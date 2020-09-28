from django.urls import path
from rest_framework_simplejwt import views as viewsJWT

from user import views

urlpatterns = [
    path("auth/jwt/refresh/", viewsJWT.TokenRefreshView.as_view()),
    path("auth/jwt/verify/", viewsJWT.TokenVerifyView.as_view()),
    path("auth/jwt/create/", views.TokenObtainPairViewCustom.as_view()),
]
