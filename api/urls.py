from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ClientAPIView

urlpatterns = [
    path('client/', ClientAPIView.as_view(), name='client'),
    path('token/', TokenObtainPairView.as_view(), name='token_ontain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]