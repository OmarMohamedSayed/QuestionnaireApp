from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .models import *
from django.db import transaction 
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from collections import Counter
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Question to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CustomerAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Question to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = CustomerAnswer.objects.all()
    serializer_class = CustomerAnswerSerializer

class CustomerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = CustomerSerializer

    def post(self, request):
        user_data = request.data
        username = user_data.get('username')
        email = user_data.pop('email')
        password = user_data.pop('password')
        user = User.objects.create(
            username=username,
            email=email,
            password=password
        )
        user.set_password(password)
        user.save()
        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)