from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LANGUAGE_CHOICES = (
        ("kor", "Korean"),
        ("eng", "English"),
    )

    CURRENCY_CHOICES = (
        ("usd", "USD"),
        ("krw", "KRW"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(null=True, choices=LANGUAGE_CHOICES, max_length=10)
    currency = models.CharField(null=True, choices=CURRENCY_CHOICES, max_length=10)
    superhost = models.BooleanField(default=False)
