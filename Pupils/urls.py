from django.urls import path

from .views import Pupils, Pupil


urlpatterns = [
    path('pupils/', Pupils, name='pupils'),
    path('pupil/<int:pk>/', Pupil, name='pupil'),
]