from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    students = Student.objects.order_by('group')
    template = 'school/students_list.html'
    context = {'students': students}


    return render(request, template, context)
