from django.shortcuts import render

# Create your views here.


def home_library_view(request):
    return render(request, 'library/home_library.html')
