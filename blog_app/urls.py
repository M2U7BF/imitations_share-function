from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
    path('home_page/<userid>', views.HomePageView.as_view(), name='home_page'),
    path('home_page/mypage/<userid>', views.MyPageView.as_view(), name='my_page'),
    path('create_article/<userid>', views.ArticleCreateView.as_view(), name='create_article'),
    path('create_user/', views.UserCreateView.as_view(), name='create_user'),
]