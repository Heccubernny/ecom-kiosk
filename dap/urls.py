from .views import *
from django.urls import path, re_path, include

app_name = 'dap'

urlpatterns = [
    path("login", LoginUserView.as_view(), name="WelcomePage"),
    path("register", RegisterUserView.as_view(), name="Registration Page"),
    path("forget", forget_password, name = "forget password"),
    path('token', token_send, name = "Token Send"),
    path('email_verified/<auth_token>', email_verified, name = "Token Send"),
   
    path('loginadmin', login_view, name = "login view"),

    path("index", HomeView.as_view(), name="WelcomePage"),

    path("shop", ShopView.as_view(), name = "Shop Page"),
    path("notfound", Error404View.as_view(), name= "Error 404 page"),
    path("about", AboutView.as_view(), name ="About page"),
    path("productpage", ProductPageView.as_view(), name = "product Page"),
    # path("", DefaultView.as_view(), name = "Default View")

    # ADMIN URL PATH
    path("loginadmin", AdminLoginView.as_view(), name="Admin Login"),
    path("home_admin", AdminHomeView.as_view(), name="Admin Index"),
    path("profileadmin", AdminProfileView.as_view(), name = "Admin Profile"),
    path('admin/', include('django.contrib.auth.urls')),

    path('add-digital-product', AddDigitalProductView.as_view(), name = "Add Digital Product")

]

