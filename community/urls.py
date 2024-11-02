from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('',views.IndexView.as_view()),
    # Blog register
    path('blogRegister/',views.blogRegisterView.as_view()),
    # BLog register successfully
    path('blogRegister/success',views.blogRegisterSuccessView.as_view()),
    path('profile/',views.profileIndexView.as_view())
]