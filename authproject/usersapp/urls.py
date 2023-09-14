from django.urls import path
from .views import LoginView, ProfileView
from rest_framework.routers import DefaultRouter
from django.urls import include
from .viewsets import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login', LoginView.as_view(), name='custom_login'),
    path('profile', ProfileView.as_view(), name='profile'),
]
