from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

import logging

logger = logging.getLogger('library')


def LoginView(request):
    """
    Handles a GET or POST request to login a user.

    If the request is a GET, renders the login template with an error message if
    any.

    If the request is a POST, attempts to authenticate the user with the given
    username and password. If the authentication is successful, logs the user in
    and redirects to the home page. If the authentication fails, renders the
    login template with an error message.

    Args:
        request (HttpRequest): The GET or POST request to login a user.

    Returns:
        HttpResponse: A redirect response to the home page if the login is
            successful, or a rendered response with an error message if the
            login fails.

    Logs an info message with the user if the login is successful.
    Logs an error message with the user and error message if the login fails.
    """
    try:
        error_message = None
        if request.method == 'POST':
            logger.info('User is attempting to login')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get(
                    'next') or 'home-library'
                logger.info('User %s logged successfully', request.user)
                return redirect(next_url)
            else:
                error_message = 'Nom d\'utilisateur ou mot de passe incorrect'
        return render(request, 'library/login.html', {'error': error_message})
    except Exception as e:
        logger.exception('An error occurred while logging in: %s', str(e))
        return redirect('login')


def LogoutView(request):
    """
    Handles a GET request to logout a user.

    Logs the user out using the built-in logout function, and redirects to the
    login page.

    Args:
        request (HttpRequest): The GET request to logout a user.

    Returns:
        HttpResponse: A redirect response to the login page.

    Logs an info message with the user if the logout is successful.
    Logs an error message with the user and error message if the logout fails.
    """
    try:
        if request.method == 'GET':
            logger.info('User %s is attempting to logout', request.user)
            logout(request)
            logger.info('User logged out successfully')
            return redirect('login')
    except Exception as e:
        logger.exception('An error occurred while logging out: %s', str(e))
