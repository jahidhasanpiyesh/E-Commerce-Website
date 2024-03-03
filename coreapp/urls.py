from django.urls import path
from coreapp import views
urlpatterns = [
    path('home/',views.home, name= 'homepage'),
    path('login/',views.user_login, name= 'user_login'),
    path('customer/',views.customer_register, name= 'customer_register'),
    path('seller/',views.seller_register, name= 'seller_register'),
    path('logout/',views.user_logout, name= 'user_logout'),
]
