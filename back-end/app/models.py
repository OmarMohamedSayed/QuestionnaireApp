from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class TimestampedModel(models.Model):
    """
    Abstract model to contain information about creation/update time.

    :created_at: date and time of record creation.
    :updated_at: date and time of any update happends for the record.
    """

    created_at = models.DateTimeField(
        verbose_name='Creation Date/Time', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Update Date/Time', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class Section(TimestampedModel):
    """
    A section has a name, a description text 
    """
    section_text = models.CharField(max_length=200)
    def __str__(self):
        return self.section_text
class Question(TimestampedModel):
    """
    A question has a name, a description text 
    """
    question_description = models.CharField(max_length=200, default='')
    question_text = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text
        
class Choice(TimestampedModel):
    """
    Each Choice contains an Choice text. Each question can have on or many Choices 
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    answer_question = models.BooleanField(default=False)
    def __str__(self):
        return self.Choice_text


class Customer(TimestampedModel):
    """
    Customer has a name, a email, a phone number,a address,  
    a nationality, a birthday, a gender 
    """
    name =models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=90, default='', blank=True)
    nationality = models.CharField(max_length=90)
    birthday = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    def __str__(self):
        return self.name


class CustomerAnswer(TimestampedModel):
    """
    CustomerAnswers has customers, questions, answers  
    """
    customersolutions= models.CharField(max_length=80)
    question =  models.ForeignKey(Question, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.customer.name

