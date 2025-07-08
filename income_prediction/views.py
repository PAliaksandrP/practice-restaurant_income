from datetime import datetime
import datetime
from .calculate import ModelPredict
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .forms import LoginForm
from .models import Results
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

model = ModelPredict()


def index(request):
    """
    Render the main index page.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered base template
    """

    logger.info('Accessed index page')
    return render(request, 'income_prediction/index.html')


def register_view(request):
    """
        Handle user registration.

        Processes registration form and creates new user account.
        Automatically logs in user after successful registration.

        Args:
            request: HttpRequest object

        Returns:
            HttpResponse: Redirect to account page on success or registration form with errors
        """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f'User {user.username} registered successfully')
            return redirect("main")
    else:
        form = RegistrationForm()
    return render(request, 'income_prediction/register.html',{'form': form})


def login_view(request):
    """
       Handle user authentication.

       Processes login form and authenticates user credentials.

       Args:
           request: HttpRequest object

       Returns:
           HttpResponse: Redirect to account page on success or login form with errors
       """
    if request.user.is_authenticated:
        logger.info('User already authenticated, redirecting to account')
        return redirect('main')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                logger.info(f'User {username} logged in successfully')
                messages.success(request, f"Welcome back, {username}!")
                return redirect('main')
            else:
                logger.warning(f'Failed login attempt for username: {username}')
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'income_prediction/login.html', {'form': form})


@login_required
def account_view(request):
    """
    Display user account information and handle password changes.

    Shows user profile, computation history and password change form.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered account template with user data
    """
    try:
        user = request.user
        results = user.results.all()[:10]  # Последние 10 результатов
        logger.debug(f'Accessing account view for user {user.username}')

        if request.method == 'POST':
            if 'change_password' in request.POST:
                password_form = CustomPasswordChangeForm(user, request.POST)
                if password_form.is_valid():
                    password_form.save()
                    update_session_auth_hash(request, user)
                    logger.info(f'Password changed for user {user.username}')
                    messages.success(request, 'Password changed successfully!')
                    return redirect('account')  # Важно: редирект после успешной смены
                # Если форма невалидна, ошибки автоматически передадутся в шаблон
            else:
                logger.warning('Password change form validation failed')
                password_form = CustomPasswordChangeForm(user)
        else:
            password_form = CustomPasswordChangeForm(user)

        return render(request, 'income_prediction/account.html', {
            'user': user,
            'password_form': password_form,
            'results': results,
        })
    except Exception as e:
        logger.error(f'Error in account_view: {str(e)}', exc_info=True)
        messages.error(request, 'Account operation error occurred')
        return redirect('main')


@login_required
def prediction_form_view(request):
    """
    Handle prediction form submission and processing.

    Processes input parameters, calculates days open, and makes revenue prediction.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Redirect to results page or prediction form with errors
    """
    if request.method == 'POST':
        form = PredictionInputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logger.debug(f'Form data received: {data}')
            # Расчет Days Open относительно 23.03.2015
            launch_date = datetime.datetime(2015, 3, 23).date()
            days_open = (launch_date - data['days_open']).days
            normalized_days_open = days_open / 1000

            # Подготовка данных для модели
            params = {
                **{f'P{i}': data.get(f'P{i}', 0.0) for i in [1, 2, 3, 4, 5, 6, 7, 11, 12, 14, 15, 17,
                                                             18, 19, 20, 21, 22, 23, 25, 27, 28, 29, 33, 37]},
                'City Group_Big Cities': 1 if data['city_group'] == 'Big Cities' else 0,
                'City Group_Other': 1 if data['city_group'] == 'Other' else 0,
                'Type_FC': 1 if data['restaurant_type'] == 'FC' else 0,
                'Type_IL': 1 if data['restaurant_type'] == 'IL' else 0,
                'Days Open': normalized_days_open
            }
            prediction_result = model.predict_result(params)
            prediction = float(prediction_result[0])
            request.session['prediction'] = prediction
            logger.info(f'Making prediction with params: {params}')
            return redirect('results')

    else:
        form = PredictionInputForm()

    return render(request, 'income_prediction/prediction_form.html', {
        'form': form
    })


@login_required
def results_view(request):
    """
    Display prediction results and save to user history.

    Retrieves prediction from session, saves to database, and displays results.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered results template with prediction data
    """
    prediction = request.session.get('prediction')
    user = request.user
    user.computations_count += 1
    user.save()
    result = Results(user=user, value=prediction)
    result.save()
    logger.info(f'Saved prediction result {prediction} for user {user.username}')
    if 'prediction' in request.session:
        del request.session['prediction']

    # Возвращаем HttpResponse с рендером шаблона
    return render(request, 'income_prediction/result.html', {
        'prediction': prediction
    })


@login_required
def logout_view(request):
    """
    Handle user logout.

    Logs out user and redirects to login page.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Redirect to login page
    """
    logout(request)
    logger.info(f'User {request.user.username} logged out successfully')
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

