from . import views
from django.urls import path

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashb', views.dashb, name='dashb'),
    path('', views.index, name='index'),
]