from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from teachers.models import Teacher


def teachers(request: HttpRequest)-> HttpResponse:
    return HttpResponse('Teachers on the main page')

def teachers(request):
    # students_of_group = Group.objects.all()
    return render(request, 'groups/groups.html', {'group': Teacher.objects.all()})