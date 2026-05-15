import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, username, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email).lower()
        user = self.model(
            email=email, 
            username=username, 
            name=name, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, name, password, **extra_fields)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    # Required fields for AbstractUser but modified for our needs
    first_name = None
    last_name = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Check if the password is NOT already a hash (prefix check).
        # This prevents double-hashing if it was already handled by the serializer or manager.
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2$')):
            self.set_password(self.password)
        super().save(*args, **kwargs)
