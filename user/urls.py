from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserDetailView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='me'),
]