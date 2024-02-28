from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home, name =''),

    path('register',views.register, name='register'),

    path('login', views.login, name='login'),

    path('user_logout', views.user_logout, name='user_logout'),
   
    #CRUD

    path('create-record', views.create_record, name='create-record'),


    path('dashboard', views.dashboard,name='dashboard'),
]