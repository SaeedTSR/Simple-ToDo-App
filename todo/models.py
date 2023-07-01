from django.db import models
from django.contrib.auth import get_user_model
import datetime

user = get_user_model()

x = datetime.datetime.today().strftime('%Y-%m-%d')
now = datetime.datetime.strptime(x, "%Y-%m-%d")
later = now + datetime.timedelta(days=10)

class Task(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('Done', 'Done'),
        ('Not yet', 'Not yet'),
    ]
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default='Not yet')
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, default=later)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
