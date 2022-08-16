
from django.contrib import admin
from admins import views as admins
from django.urls import path
from users import views as usr
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainView.index, name='index'),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path('index/', mainView.index, name='index'),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("Viewdata/", mainView.Viewdata, name="Viewdata"),

    # User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions,
         name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("viewdata/", usr.viewdata, name="viewdata"),

    # Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewRegisteredUsers/", admins.ViewRegisteredUsers,
         name="ViewRegisteredUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),
    # path("AdminDataPreProcess/", admins.AdminDataPreProcess, name="AdminDataPreProcess"),
    path("Arma", usr.Arma, name="Arma"),

]
