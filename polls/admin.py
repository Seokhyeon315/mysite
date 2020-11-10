# from django.contrib import admin
# from .models import Question, Choice

# # Register your models here.
# from .models import Question

# admin.site.register(Question)
# admin.site.register(Choice)

from django.contrib import admin 
from .models import Question, Choice

# class QuestionAdmin(admin.ModelAdmin):
#     fields=['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin) 

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

