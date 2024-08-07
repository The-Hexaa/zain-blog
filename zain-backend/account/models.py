"""
Custom User model for authentication in Django.
"""
import secrets
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+92\d{10}', message="Must be start with +92"
)
class UserManager(BaseUserManager):
    """
    User Manager
    """
    def create_user(self, email, name, role, phone_number, max_otp_out, password=None):
        """
        Creates and saves a User with the given email, name, role, and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        
        if not password:
            raise ValueError('Password must not be empty')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            role=role,
            phone_number= phone_number,
            max_otp_out= max_otp_out,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, name, and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            role='superuser',
            phone_number= '+923061050035',
            max_otp_out=timezone.now()
        )
        user.tc = True
        user.is_admin = True
        user.is_phone_verified = True
        user.is_peremium = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    Custom User Model
    """
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=(
        ('superadmin', 'superadmin'),
        ('creator', 'creator'),
        ('editor', 'editor'),
        ('client', 'client'),
    ), default='client')
    phone_number = models.CharField(
        max_length=14,
        null=False,
        blank = False,
        default='00000000000',
        validators=[phone_regex]
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=4)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_try = models.CharField(max_length=2, default=settings.MAX_OTP_TRY)
    max_otp_out = models.DateTimeField(blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    is_peremium = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, app_label): # pylint: disable=unused-argument
        """
        Does the user have a specific permission?
        """
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label): # pylint: disable=unused-argument
        """
        Does the user have permissions to view the app `app_label`?
        """
        # Simplest possible answer: Yes, always
        return True

    def generate_verification_token(self):
        """
        Generates a verification token for email verification.
        """
        self.verification_token = secrets.token_urlsafe(32)

    def verify_email(self, token):
        """
        Verifies the user's email using a verification token.
        """
        if token == self.verification_token:
            self.tc = True
            self.verification_token = ""
            self.save()
            return True
        return False

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        """
        # Simplest possible answer: All admins are staff
        return self.is_admin
# Import necessary models

