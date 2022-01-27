from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ User Model """
    class Meta:
        db_table = "user"

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (
            (GENDER_MALE, "남자"),
            (GENDER_FEMALE, "여자"),
            (GENDER_OTHER, "기타"),
        )
    )

    avatar = models.ImageField(null=True, upload_to="avatars")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="", blank=True)
