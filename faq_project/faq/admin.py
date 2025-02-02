from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import FAQ

class FAQAdmin(TranslationAdmin):
    list_display = ('question', 'question_hi', 'question_bn', 'answer', 'answer_hi', 'answer_bn')
    fieldsets = (
        ("English", {'fields': ('question', 'answer')}),
        ("Hindi", {'fields': ('question_hi', 'answer_hi')}),
        ("Bengali", {'fields': ('question_bn', 'answer_bn')}),
    )

admin.site.register(FAQ, FAQAdmin)
