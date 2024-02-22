from django.urls import path
from shopapp import views
urlpatterns = [
    path('shop/', views.shop,  name='shoppage'),
]
