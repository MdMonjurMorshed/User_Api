from django.urls import path
from .views import *
urlpatterns=[
    path('',BaseView.as_view(),name='base'),
    path('signup/',SignupForm.as_view(),name='signup-form'),
    path('user-api/',UserApiView.as_view(),name='user-create'),
    path('user-creating/',UserCreating.as_view(),name='user-creating'),
    ## login form url
    path('login/',Loginview.as_view(),name='login'),
    ## login api url
    path('login-api/',LoginApi.as_view(),name='login-api'),
    ## url for logoiut
    path('logout/',LogoutView.as_view(),name='logout'),
    path('test',TestView.as_view()),
    ## value saving url
    path('input-value',ValueSavingView.as_view(),name='input-value'),
    ## api view url
    path('input-value/api/',InputApiView.as_view(),name='input-api'),
]