from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManger(BaseUserManager):
    def create_superuser(self, student_id, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(student_id, password, **other_fields)

    def create_user(self, student_id, password, **other_fields):
        if not student_id:
            raise ValueError(_('You must provide student_id'))
        
        user = self.model(student_id=student_id, **other_fields)
        user.set_password(password)
        user.save()

        print("create user")

        return user
    
class NewUser(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(help_text="Student id", max_length=8, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # False면 email을 확인하기 전까진 비활성화 상태
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManger() # 일반/슈퍼 user 모두 처리

    USERNAME_FIELD = 'student_id' # 여기서 쓴 항목은 이미 필수 항목이므로 
    REQUIRED_FIELDS = [] # 여기서 또 쓰면 에러남

    def __str__(self):
        return self.user_name