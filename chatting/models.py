from django.db import models
from django.utils import timezone

class Message(models.Model):
    message_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)
    user_alias = models.CharField(max_length=100, default='Anonymous')

    def __str__(self):
        return self.message_text