"""
Test models - Test modellari
"""
import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Test(models.Model):
    """Test modeli"""
    
    TEST_TYPES = [
        ('diagnostic', 'Diagnostik'),
        ('formative', 'Formativ (shakllantiruvchi)'),
        ('summative', 'Summativ (yakunlovchi)'),
        ('practice', 'Mashq'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Qoralama'),
        ('published', 'Nashr qilingan'),
        ('archived', 'Arxivlangan'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Basic info
    teacher = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='created_tests',
        verbose_name=_('o\'qituvchi')
    )
    title = models.CharField(_('sarlavha'), max_length=255)
    description = models.TextField(_('tavsif'), blank=True)
    instructions = models.TextField(
        _('ko\'rsatmalar'),
        blank=True,
        help_text=_('Test boshlashdan oldin o\'quvchilarga ko\'rsatma')
    )
    
    # Classification
    subject = models.CharField(_('fan'), max_length=100, default='Informatika')
    grade = models.IntegerField(
        _('sinf'),
        choices=[(9, '9-sinf'), (10, '10-sinf')],
        default=9
    )
    test_type = models.CharField(
        _('test turi'),
        max_length=50,
        choices=TEST_TYPES,
        default='practice'
    )
    
    # Adaptive testing
    is_adaptive = models.BooleanField(
        _('adaptiv'),
        default=False,
        help_text=_('Savol qiyinligi o\'quvchi javobiga qarab o\'zgaradi')
    )
    adaptive_min_questions = models.IntegerField(
        _('minimal savollar'),
        default=15,
        help_text=_('Adaptiv testda minimal savollar soni')
    )
    adaptive_max_questions = models.IntegerField(
        _('maksimal savollar'),
        default=30,
        help_text=_('Adaptiv testda maksimal savollar soni')
    )
    
    # Questions
    questions = models.ManyToManyField(
        'questions.Question',
        through='TestQuestion',
        related_name='tests',
        verbose_name=_('savollar')
    )
    
    # Timing
    time_limit = models.IntegerField(
        _('vaqt cheklovi'),
        null=True,
        blank=True,
        help_text=_('Daqiqalarda, bo\'sh bo\'lsa - cheksiz')
    )
    
    # Schedule
    start_date = models.DateTimeField(
        _('boshlanish sanasi'),
        null=True,
        blank=True
    )
    end_date = models.DateTimeField(
        _('tugash sanasi'),
        null=True,
        blank=True
    )
    
    # Settings
    shuffle_questions = models.BooleanField(
        _('savollarni aralashtirish'),
        default=True
    )
    shuffle_options = models.BooleanField(
        _('javoblarni aralashtirish'),
        default=True
    )
    show_results_immediately = models.BooleanField(
        _('natijani darhol ko\'rsatish'),
        default=True
    )
    show_correct_answers = models.BooleanField(
        _('to\'g\'ri javoblarni ko\'rsatish'),
        default=True
    )
    allow_retake = models.BooleanField(
        _('qayta topshirishga ruxsat'),
        default=False
    )
    max_attempts = models.IntegerField(
        _('maksimal urinishlar'),
        default=1,
        validators=[MinValueValidator(1)]
    )
    
    # Passing criteria
    passing_score = models.IntegerField(
        _('o\'tish balli'),
        default=60,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Foizda')
    )
    
    # Access control
    password = models.CharField(
        _('parol'),
        max_length=100,
        blank=True,
        help_text=_('Test uchun parol (ixtiyoriy)')
    )
    allowed_students = models.ManyToManyField(
        'users.User',
        related_name='allowed_tests',
        blank=True,
        verbose_name=_('ruxsat berilgan o\'quvchilar')
    )
    
    # Status
    status = models.CharField(
        _('holat'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    # Statistics
    total_attempts = models.IntegerField(_('jami urinishlar'), default=0)
    average_score = models.FloatField(_('o\'rtacha ball'), default=0.0)
    
    # Timestamps
    created_at = models.DateTimeField(_('yaratilgan'), auto_now_add=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    published_at = models.DateTimeField(_('nashr qilingan'), null=True, blank=True)
    
    class Meta:
        db_table = 'tests'
        verbose_name = _('test')
        verbose_name_plural = _('testlar')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['teacher']),
            models.Index(fields=['status']),
            models.Index(fields=['grade', 'subject']),
            models.Index(fields=['start_date', 'end_date']),
        ]
    
    def __str__(self):
        return f"{self.title} - {self.get_grade_display()}"
    
    @property
    def total_questions(self):
        """Return total number of questions"""
        if self.is_adaptive:
            return f"{self.adaptive_min_questions}-{self.adaptive_max_questions}"
        return self.test_questions.count()
    
    @property
    def total_points(self):
        """Return total possible points"""
        return sum(tq.points for tq in self.test_questions.all())
    
    @property
    def is_active(self):
        """Check if test is currently active"""
        if self.status != 'published':
            return False
        
        from django.utils import timezone
        now = timezone.now()
        
        if self.start_date and now < self.start_date:
            return False
        if self.end_date and now > self.end_date:
            return False
        
        return True
    
    def update_statistics(self):
        """Update test statistics"""
        from apps.attempts.models import TestAttempt
        
        completed_attempts = TestAttempt.objects.filter(
            test=self,
            status='completed'
        )
        
        self.total_attempts = completed_attempts.count()
        if self.total_attempts > 0:
            avg = completed_attempts.aggregate(
                models.Avg('percentage')
            )['percentage__avg']
            self.average_score = round(avg, 2) if avg else 0.0
        
        self.save(update_fields=['total_attempts', 'average_score'])


class TestQuestion(models.Model):
    """Test va Savol o'rtasidagi bog'lanish"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test_questions',
        verbose_name=_('test')
    )
    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
        related_name='test_questions',
        verbose_name=_('savol')
    )
    
    order_number = models.IntegerField(_('tartib raqami'), default=0)
    points = models.IntegerField(
        _('ball'),
        default=1,
        validators=[MinValueValidator(0)]
    )
    
    # Override question settings for this specific test
    time_limit_override = models.IntegerField(
        _('vaqt cheklovi (bekor qilish)'),
        null=True,
        blank=True,
        help_text=_('Soniyalarda, savol uchun maxsus vaqt')
    )
    
    class Meta:
        db_table = 'test_questions'
        verbose_name = _('test savoli')
        verbose_name_plural = _('test savollari')
        ordering = ['order_number']
        unique_together = ['test', 'question']
        indexes = [
            models.Index(fields=['test', 'order_number']),
        ]
    
    def __str__(self):
        return f"{self.test.title} - Savol {self.order_number}"


class TestTemplate(models.Model):
    """Test shabloni - tez-tez ishlatiladigan test strukturasi"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('nomi'), max_length=255)
    description = models.TextField(_('tavsif'), blank=True)
    
    creator = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='test_templates',
        verbose_name=_('yaratuvchi')
    )
    
    # Template settings (JSONB)
    template_config = models.JSONField(
        _('shablon konfiguratsiyasi'),
        default=dict,
        help_text=_('Test sozlamalari va savol tanlash qoidalari')
    )
    
    is_public = models.BooleanField(_('ommaviy'), default=False)
    usage_count = models.IntegerField(_('foydalanish soni'), default=0)
    
    created_at = models.DateTimeField(_('yaratilgan'), auto_now_add=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    
    class Meta:
        db_table = 'test_templates'
        verbose_name = _('test shabloni')
        verbose_name_plural = _('test shablonlari')
        ordering = ['-usage_count', '-created_at']
    
    def __str__(self):
        return self.name
    
    def create_test_from_template(self, teacher, title=None):
        """Create a new test based on this template"""
        test = Test.objects.create(
            teacher=teacher,
            title=title or f"{self.name} - {teacher.get_full_name()}",
            **self.template_config.get('test_settings', {})
        )
        
        # Add questions based on template rules
        question_rules = self.template_config.get('question_rules', [])
        for rule in question_rules:
            questions = self._select_questions_by_rule(rule)
            for idx, question in enumerate(questions, start=1):
                TestQuestion.objects.create(
                    test=test,
                    question=question,
                    order_number=idx,
                    points=rule.get('points', 1)
                )
        
        self.usage_count += 1
        self.save(update_fields=['usage_count'])
        
        return test
    
    def _select_questions_by_rule(self, rule):
        """Select questions based on rule criteria"""
        from apps.questions.models import Question
        
        queryset = Question.objects.filter(is_active=True, is_verified=True)
        
        # Apply filters
        if 'topic' in rule:
            queryset = queryset.filter(topic=rule['topic'])
        if 'difficulty' in rule:
            queryset = queryset.filter(difficulty=rule['difficulty'])
        if 'question_type' in rule:
            queryset = queryset.filter(question_type=rule['question_type'])
        
        # Select count
        count = rule.get('count', 5)
        return queryset.order_by('?')[:count]
