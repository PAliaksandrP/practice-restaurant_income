from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    computations_count = models.PositiveIntegerField(default=0)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
# Create your models here.


class Results(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='results')
    value = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
