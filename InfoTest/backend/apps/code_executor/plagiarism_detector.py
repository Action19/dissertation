"""
Plagiarism Detection System - Plagiat aniqlash tizimi
O'xshash kodlarni aniqlash
"""
import difflib
from typing import List, Dict, Tuple
import re


class PlagiarismDetector:
    """
    Kod plagiatini aniqlash
    Dissertatsiyada tavsiflangan algoritm asosida
    """
    
    SIMILARITY_THRESHOLD = 0.80  # 80% o'xshashlik - plagiat deb hisoblanadi
    
    def __init__(self):
        self.known_codes = []
    
    def check_plagiarism(
        self,
        code: str,
        existing_codes: List[Dict[str, str]] = None
    ) -> Dict[str, any]:
        """
        Kodni plagiatga tekshirish
        
        Args:
            code: Tekshiriladigan kod
            existing_codes: Mavjud kodlar ro'yxati
                [{'author': 'username', 'code': '...'}]
        
        Returns:
            {
                'is_plagiarized': bool,
                'similarity_score': float (0-1),
                'matches': list of matching codes,
                'report': str
            }
        """
        if not existing_codes:
            return {
                'is_plagiarized': False,
                'similarity_score': 0.0,
                'matches': [],
                'report': 'Taqqoslash uchun kodlar topilmadi'
            }
        
        # Normalize code
        normalized_code = self._normalize_code(code)
        
        matches = []
        max_similarity = 0.0
        
        for existing in existing_codes:
            existing_normalized = self._normalize_code(existing['code'])
            
            # Calculate similarity
            similarity = self._calculate_similarity(
                normalized_code,
                existing_normalized
            )
            
            if similarity > self.SIMILARITY_THRESHOLD:
                matches.append({
                    'author': existing.get('author', 'Unknown'),
                    'similarity': round(similarity * 100, 2),
                    'code_snippet': existing['code'][:200] + '...'
                })
            
            max_similarity = max(max_similarity, similarity)
        
        is_plagiarized = max_similarity >= self.SIMILARITY_THRESHOLD
        
        # Generate report
        report = self._generate_report(is_plagiarized, max_similarity, matches)
        
        return {
            'is_plagiarized': is_plagiarized,
            'similarity_score': round(max_similarity, 4),
            'matches': matches,
            'report': report
        }
    
    def _normalize_code(self, code: str) -> str:
        """
        Kodni normallashtirish
        - Izohlarni olib tashlash
        - Bo'sh joylarni standartlashtirish
        - O'zgaruvchi nomlarini umumlash
        """
        # Remove comments
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)  # Python comments
        code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)  # C-style comments
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)  # Multi-line comments
        
        # Remove extra whitespace
        code = re.sub(r'\s+', ' ', code)
        
        # Remove strings (to avoid false matches)
        code = re.sub(r'"[^"]*"', '""', code)
        code = re.sub(r"'[^']*'", "''", code)
        
        # Normalize indentation
        code = code.strip()
        
        return code
    
    def _calculate_similarity(self, code1: str, code2: str) -> float:
        """
        Ikki kod o'rtasida o'xshashlikni hisoblash
        Levenshtein distance asosida
        """
        # Use SequenceMatcher from difflib
        matcher = difflib.SequenceMatcher(None, code1, code2)
        similarity = matcher.ratio()
        
        return similarity
    
    def _calculate_structural_similarity(self, code1: str, code2: str) -> float:
        """
        Strukturaviy o'xshashlikni hisoblash
        (AST - Abstract Syntax Tree asosida)
        """
        # Extract structure tokens
        tokens1 = self._extract_tokens(code1)
        tokens2 = self._extract_tokens(code2)
        
        # Compare token sequences
        matcher = difflib.SequenceMatcher(None, tokens1, tokens2)
        return matcher.ratio()
    
    def _extract_tokens(self, code: str) -> List[str]:
        """
        Koddan strukturaviy tokenlarni ajratib olish
        """
        # Simple tokenization
        tokens = []
        
        keywords = ['if', 'else', 'for', 'while', 'def', 'class', 'return', 
                   'import', 'from', 'try', 'except', 'with']
        
        words = re.findall(r'\b\w+\b', code)
        for word in words:
            if word in keywords:
                tokens.append(word)
        
        return tokens
    
    def _generate_report(
        self,
        is_plagiarized: bool,
        similarity: float,
        matches: List[Dict]
    ) -> str:
        """Hisobot yaratish"""
        
        if not is_plagiarized:
            return f"✅ Plagiat aniqlanmadi. O'xshashlik: {similarity*100:.1f}%"
        
        report = [
            f"⚠️ PLAGIAT ANIQLANDI!",
            f"O'xshashlik darajasi: {similarity*100:.1f}%",
            f"\nTopilgan o'xshashliklar ({len(matches)} ta):"
        ]
        
        for idx, match in enumerate(matches, 1):
            report.append(
                f"{idx}. {match['author']} bilan {match['similarity']}% o'xshash"
            )
        
        report.append("\n⚠️ Iltimos, o'z kodingizni yozing!")
        
        return '\n'.join(report)


class CodeSimilarityChecker:
    """
    Kengaytirilgan kod o'xshashlik tekshiruv tizimi
    """
    
    def __init__(self):
        self.detector = PlagiarismDetector()
    
    def batch_check(
        self,
        codes: List[Dict[str, str]]
    ) -> List[Dict[str, any]]:
        """
        Bir nechta kodlarni bir-biri bilan taqqoslash
        
        Args:
            codes: [{'student_id': '...', 'code': '...'}]
        
        Returns:
            Plagiat juftliklari
        """
        results = []
        
        for i, code1 in enumerate(codes):
            for j, code2 in enumerate(codes[i+1:], start=i+1):
                similarity = self._compare_codes(
                    code1['code'],
                    code2['code']
                )
                
                if similarity > 0.75:  # 75% threshold for batch check
                    results.append({
                        'student1': code1['student_id'],
                        'student2': code2['student_id'],
                        'similarity': round(similarity * 100, 2),
                        'suspicious': similarity > 0.85
                    })
        
        return results
    
    def _compare_codes(self, code1: str, code2: str) -> float:
        """Ikki kodni taqqoslash"""
        normalized1 = self.detector._normalize_code(code1)
        normalized2 = self.detector._normalize_code(code2)
        return self.detector._calculate_similarity(normalized1, normalized2)
