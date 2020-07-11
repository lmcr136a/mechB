from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)
    title = models.CharField(verbose_name='TITLE',max_length=100)
    content = models.TextField('CONTENT',default='')
    pub_date = models.DateTimeField('PUBLISH DATA',default = timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE',auto_now=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

'''
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        db_table='blog_posts'
        ordering =['-mod_date',]
        '''

'''
    def get_absolute_url(self):
       return reverse('blog:post_detail',args=(self.id,))

    def previous(self):
        return self.get_previous_by_mod_date()

    def get_next(self):
        return self.get_next_by_mod_date()
'''

