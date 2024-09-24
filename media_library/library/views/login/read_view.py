from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def LoginView(request):
    """
    View to handle user login.

    If the request is a GET, renders a login form.
    If the request is a POST, authenticate the user and log them in.
    If the authentication fails, renders the form again with errors.
    If the form is valid, logs the user in and redirects to the homepage.
    """
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home-library'
            return redirect(next_url)
        else:
            error_message = 'Nom d\'utilisateur ou mot de passe incorrect'
    return render(request, 'library/login.html', {'error': error_message})


def LogoutView(request):
    """
    View to handle user logout.

    If the request is a GET, redirects to the login page.
    """
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    # else:
    #     return redirect('home-library')
