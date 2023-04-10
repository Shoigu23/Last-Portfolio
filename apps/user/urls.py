from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', CreateUserView.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('veryfy/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='verify' )
]