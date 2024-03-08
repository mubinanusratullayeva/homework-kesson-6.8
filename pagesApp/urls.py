from django.urls import path
from .views import HomePageView, WeekdaysEnPageView, WeekdaysRuPageView, WeekdaysUzPageView

urlpatterns = [
    path('weekdays/uz', WeekdaysUzPageView.as_view(), name='weekdaysUz'),
    path('weekdays/ru', WeekdaysRuPageView.as_view(), name='weekdaysRu'),
    path('weekdays/en', WeekdaysEnPageView.as_view(), name='weekdaysEn'),
    path('', HomePageView.as_view(), name='home'),
]