from django.urls import path
from . import views

app_name = 'recommends'
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:restaurant_pk>/', views.detail , name='detail'),
] 