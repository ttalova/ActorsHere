import jwt

from datetime import datetime, timedelta

from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.models import UserManager as DjangoUserManager

from django.db import models

from authentication.enums import Role


class BaseModel(models.Model):
    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=Role.admin, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.choices, max_length=15, default=Role.user)

    @property
    def is_staff(self):
        return self.role in (Role.admin, Role.staff)

    @property
    def is_superuser(self):
        return self.role == Role.admin

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({"id": self.pk, "exp": int(dt.strftime("%s"))}, settings.SECRET_KEY, algorithm="HS256")
        # print(token)
        return token.decode("utf-8")
