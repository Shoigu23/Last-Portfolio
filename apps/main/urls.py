from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('post/<int:id>', post, name='post'),
    path('profile/', profile, name='profile'),
    path('create_post/', createPost, name='create_post'),
    path('update_post/<int:pk>', updatePost, name='update_post'),
    path('delete_post/<int:pk>', deletePost, name='delete_post'),
    path('message/', emailForm, name='message'),
    path('sendemail/', sendEmail, name='sendemail'),
]