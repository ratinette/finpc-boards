from datetime import date

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.


class Dog(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M"
        FEMALE = "F"

    class ColorChoices(models.TextChoices):
        WHITE = "WHITE"
        BLACK = "BLACK"
        BROWN = "BROWN"
        OTHERS = "OTHERS"

    name = models.CharField(max_length=50)
    birth_location = models.CharField(max_length=50)
    birthday = models.DateField()
    color = models.CharField(max_length=6, choices=ColorChoices.choices)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    owner = models.ForeignKey("DogOwner", on_delete=models.CASCADE, related_name="dogs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.birthday > date.today():
            raise ValidationError("Birthday cannot be in the future.")


class DogOwner(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
