from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about.html/',views.about,name="About Us"),
    path('brands.html/',views.brands,name="brands"),
    path('login.html/',views.loginpage,name="login"),
    path('logout.html/',views.logoutpage,name="logout"),
    path('Compare.html/',views.compare,name="compare"),
    path('Search.html/',views.search,name="search"),
    path('Comaprison.html/',views.comparison,name="comparison"),
    path('carDetails.html/<str:id>/',views.car_detail,name="car_detail"),
    #sinup:
    path('accounts/signup/',views.signup,name="signup"),


    #AJAX CAR CALLING:
    # path('carSelect/',views.ajax_car,name='AjaxCarSelect')

]