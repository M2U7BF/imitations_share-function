from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
    path('home_page/<userid>', views.HomePageView.as_view(), name='home_page'),
]