import jwt
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import User
from django.conf import settings
from .models import UserProfile


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        header = request.headers.get('Authorization')

        if header:
            token = header.split(' ')[1]
            try:
                UntypedToken(token)
                user_id = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])["user_id"]
                request.user_profile = UserProfile.objects.get(user__id=user_id)
            except (InvalidToken, User.DoesNotExist, TokenError):
                pass
        
        response = self.get_response(request)
        return response
