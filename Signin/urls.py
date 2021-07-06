from Signin import views
from django.urls import path
from . import views 
urlpatterns = [
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('register',views.register,name='register'),
    path ('',views.login,name='login' ),
    path('logout',views.logout,name='logout')
]
