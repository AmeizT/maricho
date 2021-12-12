from django.db import models
from PIL import Image
from django.db.models.expressions import Value
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class AccountUserManager(BaseUserManager):
    def create_user(self, name, surname, email, username, password=None):
        if not name:
            raise ValueError('Users must have a first name')
        if not surname:
            raise ValueError('Users must have a last name')
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, username, password=None):
        user = self.create_user(
            email=email,
            name=name,
            surname=surname,
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        max_length=255,
    )
    surname = models.CharField(
        max_length=255,
        verbose_name='surname',
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='username',
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email',
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name} {self.surname}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


def user_image_path(instance, filename):
    return 'accounts/{0}/{1}'.format(instance.id, filename)

class Account(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="account"
    )
    hexcode = models.CharField(
        max_length=255,
        blank=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'."
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=50,
        blank=True,
    )
    address = models.TextField(max_length=1000, blank=True,)
    town = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    credit = models.PositiveBigIntegerField(default=100)
    avatar = models.ImageField(default='accounts/ahvocado.png', upload_to=user_image_path)
    
    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
        ordering = ['pk']

    def __str__(self):
        return f'{self.user.name} {self.user.surname}'



