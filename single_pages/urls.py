from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name="aboutme"),
    path('', views.landing, name="landing"),
]