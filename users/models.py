import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Ensure email is required even in createsuperuser
        if not self.email:
            raise ValidationError("Email is required.")
        validate_email(self.email)
        super().save(*args, **kwargs)
