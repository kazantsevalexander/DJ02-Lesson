from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('secondary/', views.secondary, name='secondary'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
