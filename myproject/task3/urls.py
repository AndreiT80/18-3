# task3/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Глава страница
    path('page1/', views.page1, name='page1'),  # Вторая страница
    path('page2/', views.page2, name='page2'),  # Третья страница
]
