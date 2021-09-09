from django.urls import path
from heypixel.views import MyObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from heypixel import views

# from .views import UploadView



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('posts/', views.post_list.as_view()),
    path('posts/<int:pk>/', views.post_detail.as_view()),
    path('comments/', views.comment_list.as_view()),
    path('comments/<int:pk>/', views.comment_detail.as_view()),
    path('likes/', views.like_post.as_view()),
]