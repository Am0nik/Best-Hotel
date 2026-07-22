from django.urls import path
from .views import book_a_room,booking_success,admin_page,admin_login,admin_logout
urlpatterns=[
    path('book/room',book_a_room,name='book_a_room'),
    path('book/room/success',booking_success,name='booking_success'),
    path('backdoor/login',admin_login,name='admin_login'),
    path('backdoor/manage_panel/',admin_page,name='admin_page'),
    path('logout/',admin_logout,name='admin_logout'),
]