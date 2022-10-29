from django.urls import path
from . import views

app_name = 'buk2on_on'
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:restaurant_pk>/', views.detail , name='detail'),
    path('create/', views.create, name = 'create'),
    path('seoul/', views.seoul_main , name = 'seoul_main'),
    path('busan/', views.busan_main , name = 'busan_main'),

] 