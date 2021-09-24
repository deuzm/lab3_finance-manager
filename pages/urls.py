from django.urls import path
from pages import views

urlpatterns = [
    path('', views.about, name='home'),
    path('about/', views.about, name='about'),
]