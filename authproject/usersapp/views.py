from rest_framework import views, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            'token': str(refresh),
            'access': str(refresh.access_token),
        })


class ProfileView(views.APIView):
    def get(self, request):
        print(request.user_profile)

        return Response({
            'first_name': request.user_profile.first_name,
            'last_name': request.user_profile.last_name,
        })
