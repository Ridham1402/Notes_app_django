from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    tags = models.TextField()

    def __str__(self):
        return f'{self.title}'