from django.db import models
from django.conf import settings
from django.utils import timezone
from uuid import uuid4
from datetime import datetime
# Create your models here.
def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['genealogy/files', ymd_path, uuid_name])


class Fost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name='TITLE', max_length=100)
    content = models.TextField('CONTENT', default='')
    file = models.FileField(null=True, upload_to=get_file_path)
    filename = models.CharField(max_length=64, null=True, verbose_name='File name')
    pub_date = models.DateTimeField('PUBLISH DATA', default=timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE', auto_now=True)



    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()


