from django.urls import path
from coreapp import views
urlpatterns = [
    path('home/',views.home, name= 'homepage'),
]
