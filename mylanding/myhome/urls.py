from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('register.html', views.register, name= 'register'),
path('login.html', views.login, name = 'login'),
# path('booking.html', views.booking, name='booking'),
path('logout/', views.logout,name='logout'),
path('book/', views.book_room, name= 'book_room'),
path('booking_success/', views.booking_success, name='booking_success'),
path('available-rooms/', views.available_rooms, name='available_rooms'),
path('contact/', views.contact, name='contact'),
path('service/<str:service_name>/', views.service_details, name = 'service_details'),
path('mission/', views.mission, name='mission'),  
path('vision/', views.vision, name='vision'),      

    
]

