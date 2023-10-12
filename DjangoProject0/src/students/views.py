from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from django.template.loader import render_to_string


def index(request):
    data = {'title': 'Main page'}
    return render(request, 'students/index.html', context=data)


def students(request):

    all_students = Student.objects.all()
    return render(request, 'students/students.html', context={'data': all_students})
