from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView,
                         UserDestroyAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path('create_user/', UserCreateAPIView.as_view(), name='create_user'),
    path('', UserListAPIView.as_view(), name='list_users'),
    path('detail_user/<int:pk>/', UserRetrieveAPIView.as_view(),
         name='detail_user'),
    path('update_user/<int:pk>/', UserUpdateAPIView.as_view(),
         name='update_user'),
    path('delete_user/<int:pk>/', UserDestroyAPIView.as_view(),
         name='delete_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
