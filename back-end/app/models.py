from django.db import models
from django.utils import timezone

    

class Question(models.Model):
    """
    A question has a name, a description text 
    """
    question_category = models.CharField(max_length=100, default='')
    question_text = models.CharField(max_length=300)
    
    def __str__(self):
        return self.question_text
        
class Choice(models.Model):
    """
    Each Choice contains an Choice text. Each question can have on or many Choices 
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    answer_question = models.BooleanField(default=False)
    def __str__(self):
        return self.Choice_text


class Customer(models.Model):
    """
    Customer has a name, a email, a phone number,a address,  
    a nationality, a birthday, a gender 
    """
    name =models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=90, default='', blank=True)
    nationality = models.CharField(max_length=90)
    birthday = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    def __str__(self):
        return self.name

class CustomerAnswer(models.Model):
    """
    CustomerAnswers has customers, questions, answers  
    """
    customersolutions= models.CharField(max_length=80)
    question =  models.ForeignKey(Question, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.customer.name
