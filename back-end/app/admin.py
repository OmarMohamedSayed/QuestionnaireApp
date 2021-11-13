from django.contrib import admin
from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    Custom display of questions and filtering of questions by publication date. Choices can 
    be added inline (3 at a time) to choices 
    """
    fieldsets = [
        (None,               {'fields': ['question_category']}),
        (None,               {'fields': ['question_text']}),
    ]
    # add Choices in an inline fashion 
    inlines = [ChoiceInline,]
    list_display = ('question_category', 'question_text')
    # search for specific questions 
    search_fields = ['question_category']




# Add the ability to add questions and Choices to the admin view 
admin.site.register(Question, QuestionAdmin)
admin.site.register(CustomerAnswer)
admin.site.register(Customer)