from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.main_page, name='main_page'),
    path('room/create/', views.create_room, name='create_room'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('messages/', views.direct_messages, name='direct_messages'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
]
