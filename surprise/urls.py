from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('third/', views.third, name='third'),
    path('fourth/', views.fourth, name='fourth'),
    path('fifth/', views.fifth, name='fifth'),
]
