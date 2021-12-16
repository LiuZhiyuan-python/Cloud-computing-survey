from django.db import models

# Create your models here.

# GENDER_CHOICE = ((0, 'male'), (1, 'female'))
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    stu_id = models.CharField(max_length=12)
    gender = models.SmallIntegerField()
    age = models.IntegerField()
    question1 = models.CharField(max_length=200)
    question2 = models.CharField(max_length=200)


