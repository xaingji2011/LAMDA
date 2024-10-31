from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('',views.IndexView.as_view()),
    # Blog register
    path('blog/register/',views.blogRegisterView.as_view()),
    path('profile/',views.profileIndexView.as_view())
]