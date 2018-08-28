from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True)
    phone = models.CharField(
        blank=True, null=True,
        max_length=20)
    birthday = models.DateTimeField(
        blank=True, null=True)
    photo = models.ImageField(
        upload_to='user_photos',
        blank=True, null=True)
    short_desc = models.TextField(
        blank=True, null=True)

    @property
    def age(self):
        if self.birthday:
            today = timezone.now()
            months_diff = (today.month, today.day) < \
                          (self.birthday.month, self.birthday.day)
            return today.year - self.birthday.year - months_diff
        else:
            return None


@receiver(pre_save, sender=User)
def set_up_username(sender, instance, *args, **kwargs):
    instance.username = instance.email
