from django.shortcuts import render

students = [
    {'id': 1, 'name': 'Inomjon Qurbonov', 'score': 37},
    {'id': 2, 'name': 'Muhammadyusuf Abdullayev', 'score': 36},
    {'id': 3, 'name': 'Shohruhbek Turdaliyev', 'score': 29},
    {'id': 4, 'name': 'Zafarbek Olimboyev', 'score': 39},
    {'id': 5, 'name': 'Samariddin Baxtiyorov', 'score': 31},
]


# Create your views here.
def Pupils(request):
    global students
    return render(request, 'pupils.html', context={'pupils': students})


def Pupil(request, pk):
    global students
    return render(request, 'pupil.html', context={'pupil': students[pk - 1]})
