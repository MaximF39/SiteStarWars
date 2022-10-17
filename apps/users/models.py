import uuid

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
)
from django.core import validators

from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, race, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            race=race
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, username=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email if email else 'maxf39@mail.ru',
            username=username,
            password=password if password else "123123",
            race=1,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    auth_key = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(verbose_name='username', unique=True, max_length=20, null=True)

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        validators=[validators.validate_email],
        unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    money = models.IntegerField(default=0, null=False)
    race_type = (
        (1, 'Омоленианин (Красные)'),
        (2, 'Иррииец (Жёлтые)'),
        (3, 'Анид (Зелёные)'),
        (4, 'Медрамилл (Синие)'),
    )
    race = models.SmallIntegerField(verbose_name='Race', choices=race_type)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
