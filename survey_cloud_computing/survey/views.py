from django.shortcuts import render
from survey_cloud_computing.form import *
from django.http import HttpResponse
from survey.models import Answer
# Create your views here.

def survey(request):
    if request.method == 'GET':
        v = SurveyForm()
        return render(request, 'survey.html', locals())
    else:
        v = SurveyForm(request.POST)
        if v.is_valid():
            stu_id = v.cleaned_data['stu_id']
            gender = v.cleaned_data['gender']
            age = v.cleaned_data['age']
            question1 = v.cleaned_data['question1']
            question2 = v.cleaned_data['question2']
            Answer.objects.create(
                stu_id = stu_id,
                gender = gender,
                age = age,
                question1 = question1,
                question2 = question2,
            )
            print(gender)
            return HttpResponse('提交成功')
        else:
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request,'survey.html',locals())