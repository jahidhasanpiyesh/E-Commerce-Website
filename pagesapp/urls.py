from django.urls import path
from .import views
urlpatterns = [
    path('blogdetails/', views.blogdetails, name= 'blogdetails'),
    path('chackout/', views.chackout, name= 'chackout'),
    path('shopdetails/', views.shopdetails, name= 'shopdetails'),
    path('shopingcart/', views.shopingcart, name= 'shopingcart'),
]
