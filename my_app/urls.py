from django.urls import path
from my_app.views import *
urlpatterns = [
    path('',home,name="home"),
    path('login',login,name="login")
]
