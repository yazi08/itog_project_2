from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.HomeDetailView.as_view(), name = "home_page"),
    path('register/',views.RegisterUser.as_view(), name = "register"),
    path('authentication/',views.LoginUser.as_view(), name = "authentication"),
    path('client/',views.ClientView.as_view(), name = "client"),
    path('logout/',views.logout_user, name = "logout"),
    path('bot/', views.ContactFormView.as_view(), name="bot"),
    path('botik/', views.botik, name="botik"),
    path('exit/', views.exit, name="exit"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),
    path('history_table/', views.history_table, name="history_table")
]
