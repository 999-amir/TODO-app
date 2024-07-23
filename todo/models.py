from django.db import models
from accounts.models import ProfileModel


class TodoModel(models.Model):
    LEVELS = (
        ('easy', 'green'),
        ('medium', 'amber'),
        ('hard', 'red')
    )

    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, default='easy', choices=LEVELS)
    job = models.TextField(max_length=200)
    is_done = models.BooleanField(default=False)
    dead_end = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.profile)