from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    note_title  = models.CharField(max_length=200)
    note_body   = models.TextField()
    writter     = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.note_title
