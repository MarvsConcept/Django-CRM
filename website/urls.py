from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    #path('', views.login_user, name="login"),
    #path('', views.logout_user, name="logout"),
]
