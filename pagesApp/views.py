from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class WeekdaysEnPageView(TemplateView):
    template_name = 'weekdaysEn.html'

class WeekdaysRuPageView(TemplateView):
    template_name = 'weekdaysRu.html'

class WeekdaysUzPageView(TemplateView):
    template_name = 'weekdaysUz.html'
