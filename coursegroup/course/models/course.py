from django.db import models
from django.contrib.auth.models import User

class Course (models.Model):

      title = models.CharField(max_length=100)
      description = models.TextField()
      instructor = models.ForeignKey(User)

