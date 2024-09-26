from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def HomeView(request):
    """
    View to handle the homepage of the library.

    Requires the user to be logged in.

    Renders the 'library/home_library.html' template.

    :param request: the current request object
    :return: a rendered template
    """
    return render(request, 'library/home_library.html')
