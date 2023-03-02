from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager



from django.contrib.auth.validators import UnicodeUsernameValidator


class SocialNetworks(models.Model):
    name = models.CharField("Название", max_length=50)
    url = models.URLField("Ссылка", null=True, blank=True)
    slug = models.SlugField(max_length=60)
    
    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


    def __str__(self):
        return self.name



class UserManager(BaseUserManager):
    def create_user(self, username=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The given email must be set')
        username = self.normalize_email(username)
        user = self.model(username =username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)



username_validator = UnicodeUsernameValidator()
class User(AbstractUser):
    username = models.CharField(
        "Имя пользователя",
        max_length=150,
        unique=True,
        help_text=(
            "Доступно 150 символов или меньше. Только буквы, цифры и @/./+/-/_."
        ),
        validators=[username_validator],
        error_messages={
            "unique": "Пользователь с таким именем уже существует.",
        },
)
    email = None
    profile_img = models.ImageField(upload_to="users/profiles/", blank=True,null=True)
    about = models.TextField("О себе", null=True,blank=True)
    # instagram = models.URLField(null=True, blank=True)
    social_netw = models.ManyToManyField(SocialNetworks, limit_choices_to=5,)
    mobile = models.CharField("Мобильный телефон", max_length=10, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return self.username

