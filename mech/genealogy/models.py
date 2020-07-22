from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name='TITLE',max_length=100)
    content = models.TextField('CONTENT',default='')
    pub_date = models.DateTimeField('PUBLISH DATA',default = timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE',auto_now=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()
