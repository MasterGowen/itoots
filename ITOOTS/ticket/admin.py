from django.contrib import admin
from django import forms
from .models import Ticket, Attachment
from captcha.fields import CaptchaField

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
    captcha = CaptchaField()

class AttachmentAdmin(admin.ModelAdmin):
    form = AttachmentForm
    fields = ('filename', 'file')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author_email', 'id', 'date')
    form = TicketForm
    fields = [
        'subject',
        'author_name',
        'author_email',
        'text',
        'file',
        'captcha',
    ]
    readonly_fields = ['id', ]

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Attachment, AttachmentAdmin)
