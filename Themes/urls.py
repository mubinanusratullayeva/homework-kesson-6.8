from django.urls import path

from .views import Themes


urlpatterns = [
    path('themes/', Themes, name='themes'),
]