from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from random import randint

def first(request):
    return render(request, 'first.html')

def view_name(request):
    return HttpResponse('Nikas 1st HM_Django with an empty link')

def view_name1(request):
    return HttpResponse('Nikas 2nd HM_Django with http://127.0.0.1:8000/acricles link')

def view_name2(request):
    return HttpResponse('Nikas 3rd HM_Django with http://127.0.0.1:8000/acrticles/archive link')

def view_name3(request):
    return HttpResponse('Nikas 4th HM_Django with http://127.0.0.1:8000/users link')
# Create your views here.

class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def archive_view(request, art_num, slug_text=None):
    result = ''
    if (art_num % 2) == 0:
        result = 'Парне'
    else:
        result = 'Непарне'

    context = {
        'result': result,
        'text': slug_text,
        'number': randint(0, 100)
    }
    return render(request, 'index.html', context)
