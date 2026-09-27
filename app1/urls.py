from django.urls import path   
from . import views

urlpatterns = [
    path('', views.index, name="landingpage"),    
    path('login', views.login_method),
    path('view/<int:matchid>' , views.view_matches),
    path('loginPost' , views.login),
    path('profile' , views.profile, name = "p"),
    path('home' , views.home, name = "homepage"),
    path('viewallusers'  , views.viewusers),
    path('createuser' , views.createuserview),
    path('create' , views.createuser)
]