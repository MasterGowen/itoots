from django.db import models
from django.utils.html import format_html
import hashlib
from os import urandom, path
import uuid
import time


def key():
    return hashlib.md5(urandom(128)).hexdigest()


def generate_new_filename(instance, filename):
    f, ext = path.splitext(filename)
    filename = '%s%s' % (uuid.uuid4().hex, ext)
    fullpath = 'files/' + time.strftime('%Y/%m') + '/' + filename
    return fullpath


class Attachment(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default='None')
    filename = models.CharField('Filename:', max_length=255, null=True)
    file = models.FileField(upload_to=generate_new_filename)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.filename

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Attachment, self).save()


class Ticket(models.Model):

    STATUS = (
        ('0', 'Registered'),
        ('1', 'Open'),
        ('2', 'Confirmed'),
        ('3', 'Not confirmed'),
        ('4', 'In work'),
        ('5', 'Done'),
        ('6', 'Need confirmation')
    )

    id = models.CharField(max_length=32, primary_key=True, default='None')
    subject = models.CharField(max_length=1024, null=True)
    author_email = models.EmailField(null=True)
    author_name = models.CharField(max_length=64, null=True)
    text = models.TextField(max_length=4096, null=True)
    file = models.ForeignKey(Attachment)
    date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS, default='0')

    def __str__(self):
        return self.subject[:20]

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Ticket, self).save()

    def status_view(self):

        if self.status == '0':
            return format_html('<strong><span style="color:red;">{}</span></strong>',
                               self.get_status_display())
        elif self.status == '1':
            return format_html('<strong><span style="color:green;">{}</span></strong>',
                               self.get_status_display())
        elif self.status == '2':
            return format_html('<strong><span style="color:green;">{}</span></strong>',
                               self.get_status_display())
        elif self.status == '3':
            return format_html('<strong><span style="color:grey;">{}</span></strong>',
                               self.get_status_display())
        elif self.status == '4':
            return format_html('<strong><span style="color:blue;">{}</span></strong>',
                               self.get_status_display())
        elif self.status == '5':
            return format_html('<strong><span style="color:slategray;">{}</span></strong>',
                               self.get_status_display())
        elif self.status == '6':
            return format_html('<strong><span style="color:yellow;">{}</span></strong>',
                               self.get_status_display())
        else:
            return self.status

    status_view.allow_tags = True
