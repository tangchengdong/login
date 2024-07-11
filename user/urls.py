from django.urls import path

from user.views import RegisterView, LoginView, MeView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name= 'signin'),
    path('me/', MeView.as_view(), name='me'),
]