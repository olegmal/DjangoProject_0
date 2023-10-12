from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from groups.models import Group


# def groups(request: HttpRequest)-> HttpResponse:
#     return HttpResponse('Groups on the page')

def groups(request):
    # students_of_group = Group.objects.all()
    return render(request, 'groups/groups.html', {'group': Group.objects.all()})
