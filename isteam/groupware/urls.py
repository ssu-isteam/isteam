from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Register.as_view(template_name='register.html'), name='register')
]