from django.shortcuts import render

# Create your views here.
def Themes(request):
    return render(request, 'themes.html')