from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'index.html')


def me_view(request):
    return render(request, 'me.html')


def home():
    return None

def teacher_view(request):
    return render(request, 'teacher.html')