from django.db import models
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
    id = models.CharField(max_length=32, primary_key=True, default='None')
    subject = models.CharField(max_length=1024, null=True)
    author_email = models.EmailField(null=True)
    author_name = models.CharField(max_length=64, null=True)
    text = models.TextField(max_length=4096, null=True)
    file = models.ForeignKey(Attachment)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.subject[:20]

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Ticket, self).save()
