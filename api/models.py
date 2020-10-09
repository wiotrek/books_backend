from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Book(models.Model):
    GENRE = (
        (0, 'Unknown'),
        (1, 'Horror'),
        (2, 'Sci-Fi'),
        (3, 'Drama'),
        (4, 'Comedy'),
        (5, 'Fantasy'),
        (6, 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=32, blank=False)
    description = models.TextField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    genre = models.IntegerField(choices=GENRE, blank=True, null=True)
    amount_sites = models.PositiveSmallIntegerField(blank=True, null=True)
    author = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title
