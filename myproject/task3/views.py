# task3/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')


def page1(request):
    items = {
        'item1': 'Atomic War',
        'item2': 'Cyberpunk2',
        'item4': 'Мир танков'
    }
    return render(request, 'third_task/page1.html', {'items': items})


def page2(request):
    return render(request, 'third_task/page2.html')








