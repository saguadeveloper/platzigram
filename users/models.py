from django.db import models

"""Creating model for this app"""
from django.contrib.auth.models import User


class Profile(models.Model):
    """Creating profile extends base user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True, max_length=200)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username
