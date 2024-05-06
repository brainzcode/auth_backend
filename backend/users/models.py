import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserAccountManager(BaseUserManager):
    def _create_user(self, first_name, last_name, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email).lower().replace(" ", "")

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, first_name=None, last_name=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(first_name, last_name, email, password, **extra_fields)

    def create_superuser(
        self, first_name=None, last_name=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(first_name, last_name, email, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    # avatar = models.ImageField(upload_to="uploads/avatars", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # def avatar_url(self):
    #     if self.avatar:
    #         return f"{settings.WEBSITE_URL}{self.avatar.url}"
    #     else:
    #         return self.email

    def __str__(self):
        return self.email
