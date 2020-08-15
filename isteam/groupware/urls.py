from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
]