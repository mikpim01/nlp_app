from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('regex/', views.regex, name='regex'),
    path('lemo/', views.lemo, name='lemo'),
    path('pos/', views.pos, name='pos'),
    path('ner/', views.ner, name='ner'),

]
