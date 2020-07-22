from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Bmember(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    studentID = models.TextField('CONTENT', default='', max_length=10)
    signup_date = models.DateTimeField('SIGHUP DATA', default=timezone.now)
