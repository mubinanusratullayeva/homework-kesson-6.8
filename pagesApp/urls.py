from django.urls import path
from .views import HomePageView, WeekdaysPageView

urlpatterns = [
    path('weekdays/', WeekdaysPageView.as_view(), name='weekdays'),
    path('', HomePageView.as_view(), name='home'),
]