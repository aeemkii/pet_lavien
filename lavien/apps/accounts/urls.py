from django.urls import path 
from apps.accounts import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name = "login"),
    path('logout/', views.user_logut, name= "logout"), 
    path('register/', views.UserRegisterView.as_view(), name= "register"), 
    path('register/done/', views.RegisterDone.as_view(), name= "register_done")
]