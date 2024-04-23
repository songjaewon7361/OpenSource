# tdApp/models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True) #날짜 선택
    def __str__(self):
        return self.title
