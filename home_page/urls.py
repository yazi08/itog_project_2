from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.HomeDetailView.as_view(), name = "home_page"),
    path('register/',views.RegisterUser.as_view(), name = "register"),
    path('authentication/',views.LoginUser.as_view(), name = "authentication"),
    path('client/',views.client, name = "client"),

]
