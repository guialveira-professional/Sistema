from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializer import UserSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class Signin(Base):
    def post(self, request) -> Response:
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.signin(self, email = email, password = password)

        enterprise = self.get_enterprise_user(user.id)

        token = RefreshToken.for_user(user)

        serializer = UserSerializer(user)

        return Response({
            'user' : serializer.data,
            'enterprise' : enterprise,
            'refresh' : str(token),
            'access': str(token.access_token)
        })




