from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="main"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("account/", views.account_view, name="account"),
    path("prediction_form/", views.prediction_form_view, name="prediction_form"),
    path("results/", views.results_view, name="results"),
    path("logout/", views.logout_view, name="logout")
]