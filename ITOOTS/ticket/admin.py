from django.contrib import admin
from reversion.admin import VersionAdmin
from django import forms
from .models import Ticket, Attachment, Action
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
    list_display = ('filename', 'date', 'file')
    form = AttachmentForm
    fields = ('filename', 'file')


class TicketAdmin(VersionAdmin):

    list_display = ('subject', 'author_email', 'id', 'date', 'status_view')
    form = TicketForm
    fields = [
        'subject',
        'author_name',
        'author_email',
        'text',
        'file',
        'status',
        'captcha',
    ]
    readonly_fields = ['id', 'date']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Action)
