"""
Code Execution Engine - Kod bajarish tizimi
Xavfsiz Docker container ichida kod ishga tushirish
"""
import docker
import tempfile
import os
import json
import time
from typing import Dict, Any, List, Tuple
from django.conf import settings


class CodeExecutor:
    """
    Xavfsiz kod bajarish tizimi
    Dissertatsiyada ta'riflangan xavfsizlik talablariga muvofiq
    """
    
    SUPPORTED_LANGUAGES = {
        'python': {
            'image': 'python:3.10-alpine',
            'file_extension': '.py',
            'command': 'python',
            'timeout': 5,
        },
        'javascript': {
            'image': 'node:18-alpine',
            'file_extension': '.js',
            'command': 'node',
            'timeout': 5,
        },
        'java': {
            'image': 'openjdk:17-alpine',
            'file_extension': '.java',
            'command': 'java',
            'timeout': 10,
        },
        'cpp': {
            'image': 'gcc:12-alpine',
            'file_extension': '.cpp',
            'command': 'g++',
            'compile': True,
            'timeout': 10,
        },
    }
    
    def __init__(self):
        """Initialize Docker client"""
        try:
            self.client = docker.from_env()
        except Exception as e:
            raise Exception(f"Docker ulanishida xato: {str(e)}")
    
    def execute_code(
        self,
        code: str,
        language: str,
        test_cases: List[Dict[str, Any]] = None,
        timeout: int = None
    ) -> Dict[str, Any]:
        """
        Kodni bajarish va natijani qaytarish
        
        Args:
            code: Bajarilishi kerak bo'lgan kod
            language: Dasturlash tili
            test_cases: Test holatlari ro'yxati
            timeout: Maksimal bajarilish vaqti (soniya)
        
        Returns:
            Natija dictionary:
            {
                'success': bool,
                'output': str,
                'error': str,
                'execution_time': float,
                'test_results': list,
                'memory_used': int
            }
        """
        if language not in self.SUPPORTED_LANGUAGES:
            return {
                'success': False,
                'error': f"Qo'llab-quvvatlanmaydigan til: {language}"
            }
        
        lang_config = self.SUPPORTED_LANGUAGES[language]
        timeout = timeout or lang_config['timeout']
        
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(
                mode='w',
                suffix=lang_config['file_extension'],
                delete=False
            ) as f:
                f.write(code)
                temp_file = f.name
            
            # Execute code
            if test_cases:
                results = self._execute_with_tests(
                    temp_file,
                    language,
                    test_cases,
                    timeout
                )
            else:
                results = self._execute_simple(
                    temp_file,
                    language,
                    timeout
                )
            
            return results
            
        except Exception as e:
            return {
                'success': False,
                'error': f"Bajarishda xato: {str(e)}"
            }
        finally:
            # Cleanup
            if 'temp_file' in locals():
                try:
                    os.unlink(temp_file)
                except:
                    pass
    
    def _execute_simple(
        self,
        file_path: str,
        language: str,
        timeout: int
    ) -> Dict[str, Any]:
        """Oddiy bajarilish (test holatlarsiz)"""
        
        lang_config = self.SUPPORTED_LANGUAGES[language]
        
        # Read code file
        with open(file_path, 'r') as f:
            code = f.read()
        
        start_time = time.time()
        
        try:
            # Run in Docker container
            container = self.client.containers.run(
                image=lang_config['image'],
                command=f"{lang_config['command']} /code/{os.path.basename(file_path)}",
                volumes={
                    os.path.dirname(file_path): {
                        'bind': '/code',
                        'mode': 'ro'
                    }
                },
                network_disabled=True,  # Xavfsizlik
                mem_limit='128m',  # 128 MB RAM cheklovi
                cpu_quota=50000,  # CPU cheklovi
                detach=False,
                remove=True,
                timeout=timeout,
            )
            
            execution_time = time.time() - start_time
            output = container.decode('utf-8')
            
            return {
                'success': True,
                'output': output,
                'error': '',
                'execution_time': execution_time,
                'test_results': [],
                'memory_used': 0
            }
            
        except docker.errors.ContainerError as e:
            return {
                'success': False,
                'output': '',
                'error': e.stderr.decode('utf-8') if e.stderr else str(e),
                'execution_time': time.time() - start_time,
                'test_results': [],
                'memory_used': 0
            }
        except Exception as e:
            return {
                'success': False,
                'output': '',
                'error': str(e),
                'execution_time': time.time() - start_time,
                'test_results': [],
                'memory_used': 0
            }
    
    def _execute_with_tests(
        self,
        file_path: str,
        language: str,
        test_cases: List[Dict[str, Any]],
        timeout: int
    ) -> Dict[str, Any]:
        """Test holatlari bilan bajarilish"""
        
        test_results = []
        total_passed = 0
        
        for idx, test_case in enumerate(test_cases, 1):
            input_data = test_case.get('input', '')
            expected_output = test_case.get('expected_output', '')
            
            # Execute with input
            result = self._execute_with_input(
                file_path,
                language,
                input_data,
                timeout
            )
            
            # Check if output matches expected
            actual_output = result.get('output', '').strip()
            expected_output = str(expected_output).strip()
            
            passed = actual_output == expected_output
            if passed:
                total_passed += 1
            
            test_results.append({
                'test_number': idx,
                'input': input_data,
                'expected_output': expected_output,
                'actual_output': actual_output,
                'passed': passed,
                'error': result.get('error', '')
            })
        
        return {
            'success': total_passed == len(test_cases),
            'output': f"{total_passed}/{len(test_cases)} test o'tdi",
            'error': '' if total_passed == len(test_cases) else 'Ba\'zi testlar o\'tmadi',
            'execution_time': 0,
            'test_results': test_results,
            'total_tests': len(test_cases),
            'passed_tests': total_passed,
            'memory_used': 0
        }
    
    def _execute_with_input(
        self,
        file_path: str,
        language: str,
        input_data: str,
        timeout: int
    ) -> Dict[str, Any]:
        """Input bilan bajarilish"""
        
        lang_config = self.SUPPORTED_LANGUAGES[language]
        
        try:
            container = self.client.containers.run(
                image=lang_config['image'],
                command=f"sh -c 'echo \"{input_data}\" | {lang_config['command']} /code/{os.path.basename(file_path)}'",
                volumes={
                    os.path.dirname(file_path): {
                        'bind': '/code',
                        'mode': 'ro'
                    }
                },
                network_disabled=True,
                mem_limit='128m',
                cpu_quota=50000,
                detach=False,
                remove=True,
                timeout=timeout,
            )
            
            output = container.decode('utf-8')
            
            return {
                'success': True,
                'output': output,
                'error': ''
            }
            
        except docker.errors.ContainerError as e:
            return {
                'success': False,
                'output': '',
                'error': e.stderr.decode('utf-8') if e.stderr else str(e)
            }
        except Exception as e:
            return {
                'success': False,
                'output': '',
                'error': str(e)
            }


class CodeGrader:
    """
    Kod baholash tizimi
    Dissertatsiyada tavsiflangan baholash mezonlariga muvofiq
    """
    
    def __init__(self):
        self.executor = CodeExecutor()
    
    def grade_code(
        self,
        code: str,
        language: str,
        test_cases: List[Dict[str, Any]],
        grading_criteria: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Kodni to'liq baholash
        
        Returns:
            {
                'total_score': float (0-100),
                'correctness_score': float,
                'efficiency_score': float,
                'style_score': float,
                'test_results': list,
                'feedback': str
            }
        """
        # Execute code
        execution_result = self.executor.execute_code(
            code,
            language,
            test_cases
        )
        
        # Calculate correctness score (70%)
        if execution_result.get('test_results'):
            passed = execution_result.get('passed_tests', 0)
            total = execution_result.get('total_tests', 1)
            correctness_score = (passed / total) * 70
        else:
            correctness_score = 70 if execution_result.get('success') else 0
        
        # Calculate efficiency score (15%)
        efficiency_score = self._evaluate_efficiency(
            code,
            execution_result.get('execution_time', 0)
        )
        
        # Calculate style score (15%)
        style_score = self._evaluate_style(code, language)
        
        # Total score
        total_score = correctness_score + efficiency_score + style_score
        
        # Generate feedback
        feedback = self._generate_feedback(
            correctness_score,
            efficiency_score,
            style_score,
            execution_result
        )
        
        return {
            'total_score': round(total_score, 2),
            'correctness_score': round(correctness_score, 2),
            'efficiency_score': round(efficiency_score, 2),
            'style_score': round(style_score, 2),
            'test_results': execution_result.get('test_results', []),
            'feedback': feedback,
            'execution_result': execution_result
        }
    
    def _evaluate_efficiency(self, code: str, execution_time: float) -> float:
        """Kod samaradorligini baholash (0-15 ball)"""
        
        # Time-based scoring
        if execution_time < 0.1:
            time_score = 10
        elif execution_time < 0.5:
            time_score = 8
        elif execution_time < 1.0:
            time_score = 6
        elif execution_time < 2.0:
            time_score = 4
        else:
            time_score = 2
        
        # Code complexity (simple heuristic)
        lines = len(code.split('\n'))
        if lines < 10:
            complexity_score = 5
        elif lines < 20:
            complexity_score = 4
        elif lines < 50:
            complexity_score = 3
        else:
            complexity_score = 2
        
        return time_score + complexity_score
    
    def _evaluate_style(self, code: str, language: str) -> float:
        """Kod uslubini baholash (0-15 ball)"""
        
        score = 0
        
        # Check indentation
        if self._has_consistent_indentation(code):
            score += 3
        
        # Check comments
        if self._has_comments(code):
            score += 3
        
        # Check meaningful variable names
        if self._has_meaningful_names(code):
            score += 3
        
        # Check line length
        if self._check_line_length(code):
            score += 3
        
        # Check no hardcoded values (magic numbers)
        if self._no_magic_numbers(code):
            score += 3
        
        return score
    
    def _has_consistent_indentation(self, code: str) -> bool:
        """Izchil indentatsiya tekshirish"""
        lines = [l for l in code.split('\n') if l.strip()]
        if not lines:
            return True
        
        # Check if all indented lines use same indentation
        indents = set()
        for line in lines:
            if line[0] == ' ':
                indent = len(line) - len(line.lstrip())
                if indent > 0:
                    indents.add(indent % 4 if indent >= 4 else indent)
        
        return len(indents) <= 1
    
    def _has_comments(self, code: str) -> bool:
        """Izohlar mavjudligini tekshirish"""
        return '#' in code or '//' in code or '/*' in code
    
    def _has_meaningful_names(self, code: str) -> bool:
        """Ma'noli o'zgaruvchi nomlarini tekshirish"""
        # Simple heuristic: check for single-letter variable names
        single_letters = ['x', 'y', 'z', 'i', 'j', 'k']  # allowed single letters
        words = code.split()
        
        single_var_count = 0
        for word in words:
            if len(word) == 1 and word.isalpha() and word not in single_letters:
                single_var_count += 1
        
        # If less than 20% single letter vars, consider meaningful
        return single_var_count < len(words) * 0.2
    
    def _check_line_length(self, code: str) -> bool:
        """Qator uzunligini tekshirish (maksimal 80-100 belgili)"""
        lines = code.split('\n')
        long_lines = [l for l in lines if len(l) > 100]
        return len(long_lines) == 0
    
    def _no_magic_numbers(self, code: str) -> bool:
        """Hardcoded raqamlarni tekshirish"""
        import re
        # Find all numbers except 0, 1, 2 (commonly used)
        numbers = re.findall(r'\b\d+\b', code)
        magic_numbers = [n for n in numbers if int(n) > 2]
        return len(magic_numbers) < 3
    
    def _generate_feedback(
        self,
        correctness: float,
        efficiency: float,
        style: float,
        execution_result: Dict
    ) -> str:
        """Qayta aloqa yaratish"""
        
        feedback = []
        
        # Correctness feedback
        if correctness >= 60:
            feedback.append("✅ To'g'rilik: A'lo! Barcha yoki ko'pchilik testlar o'tdi.")
        elif correctness >= 40:
            feedback.append("⚠️ To'g'rilik: Yaxshi, lekin ba'zi testlar o'tmadi. Qayta tekshiring.")
        else:
            feedback.append("❌ To'g'rilik: Ko'plab xatolar. Mantiqni qayta ko'rib chiqing.")
        
        # Efficiency feedback
        if efficiency >= 12:
            feedback.append("✅ Samaradorlik: Kod tez va qisqa.")
        elif efficiency >= 8:
            feedback.append("⚠️ Samaradorlik: Optimallashtirilishi mumkin.")
        else:
            feedback.append("❌ Samaradorlik: Juda sekin yoki murakkab.")
        
        # Style feedback
        if style >= 12:
            feedback.append("✅ Uslub: Kod o'qilishi oson va yaxshi formatlangan.")
        elif style >= 8:
            feedback.append("⚠️ Uslub: Izoh va formatni yaxshilang.")
        else:
            feedback.append("❌ Uslub: Ko'proq izoh va yaxshi nomenklatura zarur.")
        
        # Test results feedback
        if execution_result.get('test_results'):
            failed_tests = [
                t for t in execution_result['test_results'] 
                if not t['passed']
            ]
            if failed_tests:
                feedback.append(f"\n📝 {len(failed_tests)} ta test o'tmadi:")
                for test in failed_tests[:3]:  # Show first 3
                    feedback.append(
                        f"  Test {test['test_number']}: "
                        f"Kutilgan '{test['expected_output']}', "
                        f"Olindi '{test['actual_output']}'"
                    )
        
        return '\n'.join(feedback)
