from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

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
    due_date = models.DateField(null=True, help_text='yyyy-mm-dd')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
