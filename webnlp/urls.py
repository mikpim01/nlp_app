from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('regex/', views.regex, name='regex'),
    path('lemma/', views.lemma, name='lemma'),
    path('pos/', views.pos, name='pos'),
    path('ner/', views.ner, name='ner'),

]
