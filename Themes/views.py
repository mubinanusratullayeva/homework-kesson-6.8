import os.path

from django.shortcuts import render


# Create your views here.

def Themes(request):
    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, 'lessons.txt')
    with open(file_path, 'r') as f:
        themes = f.read().splitlines()
    return render(request, 'themes.html', context={'lessons': themes})
