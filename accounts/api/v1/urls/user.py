from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = 'user'

urlpatterns = [
    path('registraion/', views.RegistrationAPIView.as_view(), name='signup'),
    path('activation/confirm/<str:token>', views.ActivationAPIView.as_view(), name='activation'),
    path('activation/resend/', views.ActivationResendAPIView.as_view(), name='activation-resend'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify')
]