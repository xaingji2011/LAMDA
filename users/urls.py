from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.loginView.as_view()),
    path('register/',views.registerView.as_view()),
    path('logout/',views.logoutView.as_view()),
    path('captcha/',views.sendCaptcha),
]