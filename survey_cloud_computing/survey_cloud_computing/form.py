from django import forms
from survey.models import *

class SurveyForm(forms.Form):
    stu_id = forms.CharField(max_length=10, label = '学号')
    choices = [(1,'男'),(2,'女')]
    gender = forms.ChoiceField(choices=choices,label = '性别')
    age = forms.IntegerField()
    question1 = forms.CharField(label = '你使用过盗版软件吗？')
    question2 = forms.CharField(label = '如果有，是哪些呢？')
