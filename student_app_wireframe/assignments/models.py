from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    due_date = models.DateField()
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=10,
        choices=[
            ('high', 'High'),
            ('medium', 'Medium'),
            ('low', 'Low'),
        ],
        default='medium'
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title