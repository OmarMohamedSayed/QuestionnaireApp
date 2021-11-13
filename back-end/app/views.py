from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from django.db import transaction 
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from collections import Counter

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customer to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Question to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CustomerAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Question to be viewed or edited.
    """
    queryset = CustomerAnswer.objects.all()
    serializer_class = CustomerAnswerSerializer


    def list(self, request, pk=None): 
        if pk:  
            answers = CustomerAnswer.objects.filter(question=pk)
            serializer = self.serializer_class(answers, many=True)
            countlist = [] 
            for i in serializer.data:
                countlist.append(i["customersolutions"])
            
            countlist = Counter(countlist)
            return Response(countlist)
        return HttpResponseNotFound("Page not found")