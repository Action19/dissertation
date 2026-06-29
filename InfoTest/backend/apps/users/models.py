"""
User model - Foydalanuvchi modeli
"""
import uuid
from django.contrib.auth.models.AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Custom user manager"""
    
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a regular user"""
        if not email:
            raise ValueError(_('Email manzil kiritilishi shart'))
        if not username:
            raise ValueError(_('Username kiritilishi shart'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser is_staff=True bo\'lishi kerak'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser is_superuser=True bo\'lishi kerak'))
        
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    
    ROLE_CHOICES = [
        ('student', 'O\'quvchi'),
        ('teacher', 'O\'qituvchi'),
        ('admin', 'Administrator'),
        ('parent', 'Ota-ona'),
    ]
    
    GRADE_CHOICES = [
        (9, '9-sinf'),
        (10, '10-sinf'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_('username'), max_length=150, unique=True)
    email = models.EmailField(_('email'), unique=True)
    
    first_name = models.CharField(_('ism'), max_length=150, blank=True)
    last_name = models.CharField(_('familiya'), max_length=150, blank=True)
    middle_name = models.CharField(_('otasining ismi'), max_length=150, blank=True)
    
    role = models.CharField(_('rol'), max_length=20, choices=ROLE_CHOICES)
    school = models.ForeignKey(
        'schools.School',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name=_('maktab')
    )
    grade = models.IntegerField(
        _('sinf'),
        choices=GRADE_CHOICES,
        null=True,
        blank=True
    )
    
    avatar = models.ImageField(
        _('avatar'),
        upload_to='avatars/',
        null=True,
        blank=True
    )
    phone = models.CharField(_('telefon'), max_length=20, blank=True)
    birth_date = models.DateField(_('tug\'ilgan sana'), null=True, blank=True)
    
    language = models.CharField(_('til'), max_length=10, default='uz')
    timezone = models.CharField(_('vaqt zonasi'), max_length=50, default='Asia/Tashkent')
    
    # Gamification fields
    total_points = models.IntegerField(_('jami ballar'), default=0)
    level = models.IntegerField(_('daraja'), default=1)
    experience_points = models.IntegerField(_('tajriba ballari'), default=0)
    
    # Status fields
    is_active = models.BooleanField(_('faol'), default=True)
    is_staff = models.BooleanField(_('xodim'), default=False)
    is_verified = models.BooleanField(_('tasdiqlangan'), default=False)
    
    # Timestamps
    date_joined = models.DateTimeField(_('qo\'shilgan sana'), auto_now_add=True)
    last_login = models.DateTimeField(_('oxirgi kirish'), null=True, blank=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = 'users'
        verbose_name = _('foydalanuvchi')
        verbose_name_plural = _('foydalanuvchilar')
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['role']),
            models.Index(fields=['school', 'grade']),
        ]
    
    def __str__(self):
        return f"{self.get_full_name()} (@{self.username})"
    
    def get_full_name(self):
        """Return full name"""
        if self.first_name and self.last_name:
            return f"{self.last_name} {self.first_name}"
        return self.username
    
    def get_short_name(self):
        """Return short name"""
        return self.first_name or self.username
    
    @property
    def is_student(self):
        """Check if user is student"""
        return self.role == 'student'
    
    @property
    def is_teacher(self):
        """Check if user is teacher"""
        return self.role == 'teacher'
    
    @property
    def is_admin(self):
        """Check if user is admin"""
        return self.role == 'admin' or self.is_superuser
    
    @property
    def is_parent(self):
        """Check if user is parent"""
        return self.role == 'parent'
    
    @property
    def level_name(self):
        """Return level name based on points"""
        if self.total_points < 500:
            return 'Boshlang\'ich'
        elif self.total_points < 1000:
            return 'O\'rta'
        elif self.total_points < 2000:
            return 'Yuqori'
        else:
            return 'Expert'
    
    @property
    def next_level_points(self):
        """Return points needed for next level"""
        thresholds = [500, 1000, 2000]
        for threshold in thresholds:
            if self.total_points < threshold:
                return threshold - self.total_points
        return 0
    
    def add_points(self, points):
        """Add points to user"""
        self.total_points += points
        self.experience_points += points
        
        # Level up logic
        old_level = self.level
        if self.total_points >= 2000:
            self.level = 4
        elif self.total_points >= 1000:
            self.level = 3
        elif self.total_points >= 500:
            self.level = 2
        else:
            self.level = 1
        
        self.save(update_fields=['total_points', 'experience_points', 'level'])
        
        # Check if leveled up
        if self.level > old_level:
            return True, self.level
        return False, self.level


class UserProfile(models.Model):
    """Extended user profile"""
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_('foydalanuvchi')
    )
    
    bio = models.TextField(_('biografiya'), blank=True)
    website = models.URLField(_('veb-sayt'), blank=True)
    
    # Social links
    telegram = models.CharField(_('Telegram'), max_length=100, blank=True)
    instagram = models.CharField(_('Instagram'), max_length=100, blank=True)
    
    # Preferences
    email_notifications = models.BooleanField(_('email xabarnomalar'), default=True)
    push_notifications = models.BooleanField(_('push xabarnomalar'), default=True)
    theme = models.CharField(
        _('mavzu'),
        max_length=20,
        choices=[('light', 'Yorug\''), ('dark', 'Qorong\'u')],
        default='light'
    )
    
    # Statistics
    tests_completed = models.IntegerField(_('topshirilgan testlar'), default=0)
    average_score = models.FloatField(_('o\'rtacha ball'), default=0.0)
    total_time_spent = models.IntegerField(_('jami vaqt (daqiqa)'), default=0)
    
    created_at = models.DateTimeField(_('yaratilgan'), auto_now_add=True)
    updated_at = models.DateTimeField(_('yangilangan'), auto_now=True)
    
    class Meta:
        db_table = 'user_profiles'
        verbose_name = _('foydalanuvchi profili')
        verbose_name_plural = _('foydalanuvchi profillari')
    
    def __str__(self):
        return f"Profile: {self.user.username}"
    
    def update_statistics(self):
        """Update user statistics"""
        from apps.attempts.models import TestAttempt
        
        attempts = TestAttempt.objects.filter(
            student=self.user,
            status='completed'
        )
        
        self.tests_completed = attempts.count()
        if self.tests_completed > 0:
            self.average_score = attempts.aggregate(
                models.Avg('percentage')
            )['percentage__avg'] or 0.0
            self.total_time_spent = attempts.aggregate(
                models.Sum('time_taken')
            )['time_taken__sum'] or 0
            self.total_time_spent = self.total_time_spent // 60  # convert to minutes
        
        self.save(update_fields=['tests_completed', 'average_score', 'total_time_spent'])
