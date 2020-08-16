from django.urls import path

from .views import GroupwareMainPage


urlpatterns = [
    path('', GroupwareMainPage.as_view(), name='groupware_main')
]