from django.contrib.auth.models import AbstractUser
from django.db import models


class UserIsDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class User(AbstractUser):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ["email", "is_deleted"]

    # objects = UserIsDeletedManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.username
