"""
IRT (Item Response Theory) Engine - Adaptiv baholash tizimi
Dissertatsiyada tavsiflangan IRT nazariyasi asosida
"""
import math
from typing import List, Dict, Tuple, Optional
import numpy as np


class IRTEngine:
    """
    IRT (Item Response Theory) asosida adaptiv test tizimi
    
    Dissertatsiyadan:
    - IRT 3-parametrli model (difficulty, discrimination, guessing)
    - O'quvchi qobiliyati (theta) ni hisoblash
    - Keyingi savol tanlash algoritmi
    """
    
    def __init__(self):
        self.theta_initial = 0.0  # Boshlang'ich qobiliyat darajasi
        self.theta_min = -3.0
        self.theta_max = 3.0
        self.convergence_threshold = 0.05
    
    def calculate_probability(
        self,
        theta: float,
        difficulty: float,
        discrimination: float,
        guessing: float = 0.25
    ) -> float:
        """
        3-parametrli IRT modeli bo'yicha to'g'ri javob ehtimolini hisoblash
        
        P(θ) = c + (1 - c) / (1 + e^(-a(θ - b)))
        
        Args:
            theta: O'quvchi qobiliyati (-3 dan +3)
            difficulty: Savol qiyinligi (b parametri)
            discrimination: Diskriminatsiya (a parametri)
            guessing: Taxmin ehtimoli (c parametri)
        
        Returns:
            Ehtimol (0 dan 1 gacha)
        """
        exponent = -discrimination * (theta - difficulty)
        probability = guessing + (1 - guessing) / (1 + math.exp(exponent))
        return probability
    
    def update_theta(
        self,
        current_theta: float,
        is_correct: bool,
        difficulty: float,
        discrimination: float,
        guessing: float = 0.25
    ) -> float:
        """
        O'quvchi javobiga qarab theta ni yangilash
        Maximum Likelihood Estimation (MLE) usuli
        
        Args:
            current_theta: Hozirgi qobiliyat darajasi
            is_correct: Javob to'g'rimi?
            difficulty: Savol qiyinligi
            discrimination: Diskriminatsiya
            guessing: Taxmin ehtimoli
        
        Returns:
            Yangilangan theta qiymati
        """
        # Calculate current probability
        p = self.calculate_probability(
            current_theta,
            difficulty,
            discrimination,
            guessing
        )
        
        # Calculate information (Fisher information)
        q = 1 - p
        numerator = (discrimination ** 2) * ((p - guessing) ** 2) * q
        denominator = p * ((1 - guessing) ** 2)
        information = numerator / denominator if denominator > 0 else 0.01
        
        # Calculate update step
        if is_correct:
            update = (1 - p) / information
        else:
            update = -p / information
        
        # Update theta
        new_theta = current_theta + update
        
        # Constrain to reasonable bounds
        new_theta = max(self.theta_min, min(self.theta_max, new_theta))
        
        return new_theta
    
    def select_next_question(
        self,
        current_theta: float,
        available_questions: List[Dict],
        answered_questions: List[str]
    ) -> Optional[Dict]:
        """
        Keyingi eng mos savolni tanlash
        Maximum Information Selection strateg usuli
        
        Args:
            current_theta: Hozirgi qobiliyat darajasi
            available_questions: Mavjud savollar
                [{'id': '...', 'difficulty': float, 'discrimination': float, ...}]
            answered_questions: Javob berilgan savol IDlari
        
        Returns:
            Eng mos savol yoki None
        """
        # Filter out already answered questions
        candidates = [
            q for q in available_questions 
            if q['id'] not in answered_questions
        ]
        
        if not candidates:
            return None
        
        # Calculate information for each question
        question_info = []
        for question in candidates:
            info = self.calculate_information(
                current_theta,
                question['difficulty'],
                question['discrimination'],
                question.get('guessing', 0.25)
            )
            question_info.append({
                'question': question,
                'information': info,
                'probability': self.calculate_probability(
                    current_theta,
                    question['difficulty'],
                    question['discrimination'],
                    question.get('guessing', 0.25)
                )
            })
        
        # Select question with maximum information
        # Prefer questions with P(θ) close to 0.5 (most informative)
        best_question = max(
            question_info,
            key=lambda x: x['information']
        )
        
        return best_question['question']
    
    def calculate_information(
        self,
        theta: float,
        difficulty: float,
        discrimination: float,
        guessing: float = 0.25
    ) -> float:
        """
        Fisher information ni hisoblash
        Savolning informatsiyaviy qiymatini baholash
        
        Returns:
            Information qiymati
        """
        p = self.calculate_probability(theta, difficulty, discrimination, guessing)
        q = 1 - p
        
        numerator = (discrimination ** 2) * ((p - guessing) ** 2) * q
        denominator = p * ((1 - guessing) ** 2)
        
        information = numerator / denominator if denominator > 0 else 0
        return information
    
    def estimate_final_theta(
        self,
        responses: List[Dict]
    ) -> Tuple[float, float]:
        """
        Barcha javoblar asosida yakuniy theta ni hisoblash
        
        Args:
            responses: Javoblar ro'yxati
                [{'is_correct': bool, 'difficulty': float, 'discrimination': float}]
        
        Returns:
            (theta, standard_error) tuple
        """
        if not responses:
            return self.theta_initial, 1.0
        
        theta = self.theta_initial
        
        # Iterative MLE
        for iteration in range(50):  # Max 50 iterations
            old_theta = theta
            
            # Update based on all responses
            total_update = 0
            total_information = 0
            
            for response in responses:
                p = self.calculate_probability(
                    theta,
                    response['difficulty'],
                    response['discrimination'],
                    response.get('guessing', 0.25)
                )
                
                info = self.calculate_information(
                    theta,
                    response['difficulty'],
                    response['discrimination'],
                    response.get('guessing', 0.25)
                )
                
                if response['is_correct']:
                    total_update += (1 - p) * info
                else:
                    total_update += -p * info
                
                total_information += info
            
            # Update theta
            if total_information > 0:
                theta += total_update / total_information
            
            # Constrain bounds
            theta = max(self.theta_min, min(self.theta_max, theta))
            
            # Check convergence
            if abs(theta - old_theta) < self.convergence_threshold:
                break
        
        # Calculate standard error
        standard_error = 1 / math.sqrt(total_information) if total_information > 0 else 1.0
        
        return theta, standard_error
    
    def theta_to_score(self, theta: float, scale: int = 100) -> float:
        """
        Theta ni oddiy ballga o'tkazish
        
        Args:
            theta: IRT theta qiymati (-3 dan +3)
            scale: Ball shkalasi (default: 100)
        
        Returns:
            Ball (0 dan scale gacha)
        """
        # Normalize theta from [-3, 3] to [0, 1]
        normalized = (theta - self.theta_min) / (self.theta_max - self.theta_min)
        
        # Scale to desired range
        score = normalized * scale
        
        return max(0, min(scale, score))
    
    def score_to_theta(self, score: float, scale: int = 100) -> float:
        """
        Oddiy ballni theta ga o'tkazish
        
        Args:
            score: Ball (0 dan scale gacha)
            scale: Ball shkalasi
        
        Returns:
            Theta qiymati
        """
        # Normalize score to [0, 1]
        normalized = score / scale
        
        # Convert to theta range
        theta = self.theta_min + normalized * (self.theta_max - self.theta_min)
        
        return theta


class AdaptiveTestController:
    """
    Adaptiv test jarayonini boshqarish
    Dissertatsiyada tavsiflangan adaptiv test logikasi
    """
    
    def __init__(
        self,
        min_questions: int = 15,
        max_questions: int = 30,
        termination_threshold: float = 0.3
    ):
        """
        Args:
            min_questions: Minimal savollar soni
            max_questions: Maksimal savollar soni
            termination_threshold: Test tugash uchun SE chegarasi
        """
        self.irt = IRTEngine()
        self.min_questions = min_questions
        self.max_questions = max_questions
        self.termination_threshold = termination_threshold
    
    def should_continue(
        self,
        answered_count: int,
        current_se: float
    ) -> bool:
        """
        Testni davom ettirishni aniqlash
        
        Returns:
            True - davom ettirish kerak
            False - test tugashi mumkin
        """
        # Must answer minimum questions
        if answered_count < self.min_questions:
            return True
        
        # Cannot exceed maximum
        if answered_count >= self.max_questions:
            return False
        
        # Check if standard error is low enough
        if current_se <= self.termination_threshold:
            return False
        
        return True
    
    def initialize_test(self) -> Dict:
        """
        Testni boshlash - boshlang'ich holatni yaratish
        
        Returns:
            Test holati
        """
        return {
            'theta': self.irt.theta_initial,
            'standard_error': 1.0,
            'responses': [],
            'answered_questions': [],
            'question_count': 0
        }
    
    def process_answer(
        self,
        test_state: Dict,
        question: Dict,
        is_correct: bool
    ) -> Dict:
        """
        Javobni qayta ishlash va holatni yangilash
        
        Args:
            test_state: Hozirgi test holati
            question: Javob berilgan savol
            is_correct: To'g'ri yoki noto'g'ri
        
        Returns:
            Yangilangan test holati
        """
        # Update theta
        new_theta = self.irt.update_theta(
            test_state['theta'],
            is_correct,
            question['difficulty'],
            question['discrimination'],
            question.get('guessing', 0.25)
        )
        
        # Add response to history
        test_state['responses'].append({
            'is_correct': is_correct,
            'difficulty': question['difficulty'],
            'discrimination': question['discrimination'],
            'guessing': question.get('guessing', 0.25)
        })
        
        test_state['answered_questions'].append(question['id'])
        test_state['question_count'] += 1
        
        # Recalculate final estimate
        final_theta, se = self.irt.estimate_final_theta(test_state['responses'])
        
        test_state['theta'] = final_theta
        test_state['standard_error'] = se
        
        return test_state
    
    def get_test_result(self, test_state: Dict) -> Dict:
        """
        Test yakuniy natijasini hisoblash
        
        Returns:
            {
                'theta': float,
                'score': float (0-100),
                'standard_error': float,
                'questions_answered': int,
                'accuracy': float
            }
        """
        theta = test_state['theta']
        score = self.irt.theta_to_score(theta)
        
        # Calculate accuracy
        correct_count = sum(1 for r in test_state['responses'] if r['is_correct'])
        accuracy = (correct_count / len(test_state['responses'])) * 100 if test_state['responses'] else 0
        
        return {
            'theta': round(theta, 4),
            'score': round(score, 2),
            'standard_error': round(test_state['standard_error'], 4),
            'questions_answered': test_state['question_count'],
            'accuracy': round(accuracy, 2),
            'level': self._get_proficiency_level(theta)
        }
    
    def _get_proficiency_level(self, theta: float) -> str:
        """
        Theta asosida malaka darajasini aniqlash
        """
        if theta < -1.5:
            return 'Boshlang\'ich'
        elif theta < 0:
            return 'O\'rta'
        elif theta < 1.5:
            return 'Yuqori'
        else:
            return 'Expert'
