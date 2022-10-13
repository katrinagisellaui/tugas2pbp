from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date = models.DateField(auto_now_add = True)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default = False)


