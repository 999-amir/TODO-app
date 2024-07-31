from rest_framework.generics import GenericAPIView
from .serializers import CostumeUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login


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
        # user = CostumeUser.objects.create_user(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        serializer.save()
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        login(request, user)
        data = {
            'msg': 'user created and logged in',
            'detail': serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)
