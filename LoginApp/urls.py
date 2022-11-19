from django.urls import path
from . import views

app_name = 'loginapp'
urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.sign_in, name='sign_in'),
    path('logout/', views.sign_out, name='sign_out'),
    path('profile/', views.UserProfile, name='profile'),
    path('ChangeUserProfile/', views.ChangeUserProfile, name='ChangeUserProfile'),
    path('password/', views.ChangePasss, name='password'),
    path('AddProPic/', views.AddProPic, name='AddProPic'),
    path('ProPicChange/', views.ProPicChange, name='ProPicChange'),

   
]