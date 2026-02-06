from django.urls import path
from papp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("compare",compare,name="compare"),
    path("details",details,name="details"),
    path("login-register",login_register,name="login-register"),
    path("shop",shop,name="shop"),
    path("wishlist",wishlist,name="wishlist"),
    
    path("user-registration",user_registration,name="user-registration"),
    path("user-login",user_login,name="user-login"),
    path("user-logout",user_logout,name="user-logout"),
    
    path("getproducts",get_products,name="getproducts"),
    path("getcategories",get_categories,name="getcategories"),
    path("searchproducts",search_products,name="searchproducts"),
    path("addtocart",addtocart,name="addtocart"),
    
    path("removecart",removecart,name="removecart"),
    path("changeqty",changeqty,name="changeqty"),
    path("payment",payment,name="payment"),
    path("makeorder",makeorder,name="makeorder"),
    path('add_address',add_address,name='add_address'),
    path('get_address',get_address,name='get_address'),
    path('forgotpass',forgotpass,name="forgotpass"),
    path("password-sendmail",password_sendmail,name="password-sendmail"),
    path("resetpass",resetpass,name="resetpass"),
]
