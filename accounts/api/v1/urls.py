from django.urls import path
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('signup/', views.SignupGenericAPIView.as_view(), name='signup'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout')
]
