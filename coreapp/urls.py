from django.urls import path
from coreapp import views
urlpatterns = [
    path('home/',views.home, name= 'homepage'),
    path('login/',views.user_login, name= 'user_login'),
    path('register/',views.user_register, name= 'user_register'),
]
