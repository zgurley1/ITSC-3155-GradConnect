from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),

    # path('direct_message/<int:recipient_id>/', views.send_direct_message, name='send_direct_message'),
    # path('direct_message/inbox/', views.view_direct_message, name='view_direct_message'),

    # path('direct_message/inbox/', views.view_direct_message, name='view_direct_message'),
    # path('direct_message/<int:recipient_id>/', views.send_direct_message, name='send_direct_message'),
    # path('direct_message/<int:recipient_id>/', views.view_direct_message_with_recipient, name='view_direct_message_with_recipient'),

    path('send_message/<int:recipient_id>/', views.send_direct_message, name='send_direct_message'),
    path('view_message/<int:recipient_id>/', views.view_direct_message_with_recipient, name='view_direct_message_with_recipient'),
]
