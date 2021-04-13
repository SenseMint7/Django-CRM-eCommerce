from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """
    유저 정보
    """
    username = username = models.CharField('유저 아이디', max_length=30)
    email = models.EmailField('이메일', unique=True)
    name = models.CharField('이름', max_length=30, blank=True)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['username']  # 필수입력값

    class Meta:
        verbose_name_plural = "유저 정보"

    def __str__(self):
        return self.item_name

