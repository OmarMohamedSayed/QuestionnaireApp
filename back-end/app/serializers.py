from .models import *
from rest_framework import serializers

class ChoiceToSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('Choice_text','answer_question')


class CustomerAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAnswer
        fields = '__all__'

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    customeranswer = CustomerAnswerSerializer(source='customeranswer_set', many=True)
    class Meta:
        model = Customer
        fields = ('name','email','phone_number','address','nationality','birthday','gender','customeranswer')

    def create(self, validated_data):
        customeranswers = validated_data.pop('customeranswer_set')
       
        customer = Customer.objects.create(**validated_data)

        for customeranswer in customeranswers:
            customeranswer['customer'] = customer
            CustomerAnswer.objects.create(**customeranswer)
        return customer

class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceToSerializer(source='choice_set', many=True)    
    class Meta:
        model = Question
        fields = ('id','question_category', 'question_text','choice')
    
    def create(self, validated_data):
        choices = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(question=question, **choice)
        return question
