from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasklist(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task+" - "+str(self.done)

class Contact(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.EmailField(max_length = 150)
    message = models.TextField()

    def __str__(self):
        return self.email_address




