from django.urls import path, include
from . import views

app_name = 'BookingsApp'

urlpatterns = [
    path('', views.home, name='Home'),
    path('reservations/create/', views.reservation_create, name='reservation_create'),
    path('reservations/list/', views.reservation_list, name='reservation_list'),
    path('rental/create/', views.rental_create, name='rental_create'),
    path('reservations/edit/<int:pk>/', views.reservation_edit, name='reservation_edit'),
    path('reservations/delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),
]
