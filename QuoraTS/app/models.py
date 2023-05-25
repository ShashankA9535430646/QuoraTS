from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    query  = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)


class Answer(models.Model):
    # id = models.PositiveIntegerField(primary_key=True,null=False)
    query_answer = models.ForeignKey(Question,related_name="answers", on_delete=models.CASCADE)
    content = models.TextField(null=True)
    likes = models.IntegerField(default=0)