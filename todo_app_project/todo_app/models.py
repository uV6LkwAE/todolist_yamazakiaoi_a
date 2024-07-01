from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY = (('finished','完了'),('unfinished','未完了'))

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    date = models.DateField()
    status = models.CharField(
        max_length = 100,
        choices = CATEGORY
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title