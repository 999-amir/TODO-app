from rest_framework.generics import GenericAPIView
from .serializers import CostumeUserSerializer, CustomAuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# SESSION
class SignupGenericAPIView(GenericAPIView):
    serializer_class = CostumeUserSerializer

    def get(self, request):
        user = self.request.user
        if user.id:
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        return Response({"detail": "need authentication"}, status=status.HTTP_200_OK)

    def post(self, request):
        if self.request.user.is_authenticated:
            return Response({'detail': 'need to logout first to create new account'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # CostumeUser.objects.create_user(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        serializer.save()
        data = {
            'msg': 'user created and logged in',
            'detail': serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)


# TOKEN
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
