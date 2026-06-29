"""
Question models - Savol modellari
Dissertatsiyaga muvofiq 8 xil savol turi qo'llab-quvvatlanadi
"""
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    """Savol modeli"""
    
    # 8 xil savol turi (dissertatsiyadan)
    QUESTION_TYPES = [
        ('single_choice', 'Bir to\'g\'ri javobli test'),
        ('multiple_choice', 'Ko\'p to\'g\'ri javobli test'),
        ('true_false', 'To\'g\'ri/Noto\'g\'ri'),
        ('matching', 'Moslashtirish'),
        ('ordering', 'Tartibga solish'),
        ('fill_blank', 'Bo\'sh joyni to\'ldirish'),
        ('short_answer', 'Qisqa javob'),
        ('code_writing', 'Kod yozish'),
    ]
    
    DIFFICULTY_LEVELS = [
        (1, 'Juda oson'),
        (2, 'Oson'),
        (3, 'O\'rtacha'),
        (4, 'Qiyin'),
        (5, 'Juda qiyin'),
    ]
    
    BLOOM_LEVELS = [
        ('knowledge', 'Bilish'),
        ('comprehension', 'Tushunish'),
        ('application', 'Qo\'llash'),
        ('analysis', 'Tahlil qilish'),
        ('synthesis', 'Sintez qilish'),
        ('evaluation', 'Baholash'),
    ]
    
    # Basic fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='authored_questions',
        verbose_name=_('muallif')
    )
    
    question_type = models.CharField(
        _('savol turi'),
        max_length=50,
        choices=QUESTION_TYPES
    )
    
    # Topic classification
    topic = models.CharField(_('mavzu'), max_length=100)
    subtopic = models.CharField(_('kichik mavzu'), max_length=100, blank=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        verbose_name=_('teglar'),
        blank=True,
        default=list,
        help_text=_('Masalan: ["python", "tsikl", "for"]')
    )
    
    # Difficulty
    difficulty = models.IntegerField(
        _('qiyinlik darajasi'),
        choices=DIFFICULTY_LEVELS,
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    bloom_level = models.CharField(
        _('Bloom darajasi'),
        max_length=50,
        choices=BLOOM_LEVELS,
        default='knowledge'
    )
    
    # Question content
    question_text = models.TextField(_('savol matni'))
    question_media_url = models.URLField(
        _('media fayl URL'),
        blank=True,
        help_text=_('Rasm, video yoki audio fayl havolasi')
    )
    question_image = models.ImageField(
        _('rasm'),
        upload_to='questions/images/',
        blank=True,
        null=True
    )
    code_snippet = models.TextField(
        _('kod namunasi'),
        blank=True,
        help_text=_('Agar dasturlash savoli bo\'lsa')
    )
    code_language = models.CharField(
        _('dasturlash tili'),
        max_length=50,
        blank=True,
        help_text=_('python, javascript, java, c++')
    )
    
    # Options (JSONB format for flexibility)
    options = models.JSONField(
        _('javob variantlari'),
        default=dict,
        help_text=_('''
        Format har xil savol turi uchun:
        single_choice/multiple_choice: {"A": "text", "B": "text", ...}
        matching: {"left": [...], "right": [...]}
        ordering: {"items": [...]}
        fill_blank: {"blanks": [...]}
        ''')
    )
    
    # Correct answer
    correct_answer = models.JSONField(
        _('to\'g\'ri javob'),
        help_text=_('''
        Format:
        single_choice: {"answer": "A"}
        multiple_choice: {"answers": ["A", "B"]}
        true_false: {"answer": true}
        matching: {"pairs": {"1": "a", "2": "b"}}
        ordering: {"order": [3, 1, 2, 4]}
        fill_blank: {"answers": ["word1", "word2"]}
        short_answer: {"answer": "text", "alternatives": [...]}
        code_writing: {"expected_output": "...", "test_cases": [...]}
        ''')
    )
    
    # Explanation and hints
    explanation = models.TextField(
        _('tushuntirish'),
        blank=True,
        help_text=_('To\'g\'ri javob uchun tushuntirish')
    )
    hints = models.TextField(
        _('maslahat'),
        blank=True,
        help_text=_('O\'quvchiga yordam')
    )
    
    # Time estimation
    estimated_time = models.IntegerField(
        _('taxminiy vaqt'),
        default=60,
        help_text=_('Soniyalarda')
    )
    
    # Statistics (IRT parameters)
    usage_count = models.IntegerField(_('foydalanish soni'), default=0)
    success_rate = models.FloatField(
        _('to\'g\'ri javob foizi'),
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )
    
    # IRT (Item Response Theory) parametrlari
    irt_difficulty = models.FloatField(
        _('IRT qiyinlik'),
        default=0.0,
        help_text=_('Adaptiv testlar uchun (-3 dan +3 gacha)')
    )
    irt_discrimination = models.FloatField(
        _('IRT diskriminatsiya'),
        default=1.0,
        help_text=_('Adaptiv testlar uchun (0 dan 2 gacha)')
    )
    irt_guessing = models.FloatField(
        _('IRT taxmin'),
        default=0.25,
        help_text=_('Tasodifiy to\'g\'ri javob ehtimoli')
    )
    
    # Status
    is_active = models.BooleanField(_('faol'), default=True)
    is_verified = models.BooleanField(_('tasdiqlangan'), default=False)
    verified_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='verified_questions',
        verbose_name=_('tasdiqlagan')
    )
    
    # Timestamps
    created_at = models.DateTimeField(_('yaratilgan'), auto_now_add=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    
    class Meta:
        db_table = 'questions'
        verbose_name = _('savol')
        verbose_name_plural = _('savollar')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['question_type']),
            models.Index(fields=['topic', 'subtopic']),
            models.Index(fields=['difficulty']),
            models.Index(fields=['is_active', 'is_verified']),
            models.Index(fields=['author']),
        ]
    
    def __str__(self):
        return f"{self.get_question_type_display()}: {self.question_text[:50]}..."
    
    def update_statistics(self, is_correct):
        """
        Update question statistics after each attempt
        """
        self.usage_count += 1
        
        # Update success rate
        if self.usage_count == 1:
            self.success_rate = 100.0 if is_correct else 0.0
        else:
            # Moving average
            old_total = self.success_rate * (self.usage_count - 1) / 100
            new_total = old_total + (1 if is_correct else 0)
            self.success_rate = (new_total / self.usage_count) * 100
        
        self.save(update_fields=['usage_count', 'success_rate'])
    
    def update_irt_parameters(self):
        """
        Update IRT parameters based on student responses
        Advanced statistical calculation (dissertatsiyada tavsiflangan)
        """
        from apps.attempts.models import Answer
        
        answers = Answer.objects.filter(question=self).select_related('attempt__student')
        
        if answers.count() < 30:  # Minimum sample size
            return
        
        # Calculate difficulty (b parameter)
        # Difficulty = logit(P) where P is proportion of correct answers
        correct_count = answers.filter(is_correct=True).count()
        total_count = answers.count()
        proportion = correct_count / total_count if total_count > 0 else 0.5
        
        # Avoid log(0) and log(1)
        proportion = max(0.01, min(0.99, proportion))
        
        import math
        self.irt_difficulty = math.log(proportion / (1 - proportion))
        
        # Calculate discrimination (a parameter)
        # Measure of how well the question differentiates students
        # Simplified approach: based on variance
        student_abilities = []
        for answer in answers:
            # Get student's average performance
            student_avg = answer.attempt.student.profile.average_score / 100.0
            student_abilities.append(student_avg)
        
        if len(student_abilities) > 1:
            import statistics
            ability_variance = statistics.variance(student_abilities)
            self.irt_discrimination = min(2.0, ability_variance * 4)
        
        self.save(update_fields=['irt_difficulty', 'irt_discrimination'])


class QuestionBank(models.Model):
    """Savol banki - savollarni guruhlash uchun"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('nomi'), max_length=255)
    description = models.TextField(_('tavsif'), blank=True)
    
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='question_banks',
        verbose_name=_('egasi')
    )
    
    questions = models.ManyToManyField(
        Question,
        related_name='banks',
        verbose_name=_('savollar'),
        blank=True
    )
    
    is_public = models.BooleanField(_('ommaviy'), default=False)
    is_official = models.BooleanField(_('rasmiy'), default=False)
    
    created_at = models.DateTimeField(_('yaratilgan'), auto_now_add=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    
    class Meta:
        db_table = 'question_banks'
        verbose_name = _('savol banki')
        verbose_name_plural = _('savol banklari')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    @property
    def question_count(self):
        return self.questions.count()


class QuestionComment(models.Model):
    """Savollarga izoh"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('savol')
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='question_comments',
        verbose_name=_('muallif')
    )
    
    content = models.TextField(_('mazmun'))
    is_resolved = models.BooleanField(_('hal qilingan'), default=False)
    
    created_at = models.DateTimeField(_('yaratilgan'), auto_now_add=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    
    class Meta:
        db_table = 'question_comments'
        verbose_name = _('savol izohi')
        verbose_name_plural = _('savol izohlari')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Izoh: {self.question} - {self.author}"
