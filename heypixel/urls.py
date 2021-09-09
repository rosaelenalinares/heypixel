from django.urls import path
from heypixel.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from heypixel import views
from django.views.generic import TemplateView
# from .views import UploadView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('profiles/', views.ProfileView.as_view()),
    path('profiles/<int:pk>/', views.ProfileViewDetail.as_view()),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('posts/', views.post_list.as_view()),
    path('posts/<int:pk>/', views.post_detail.as_view()),
    path('comments/', views.comment_list.as_view()),
    path('comments/<int:pk>/', views.comment_detail.as_view()),
    path('likes/', views.like_post.as_view()),
]