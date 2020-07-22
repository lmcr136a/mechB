from django.contrib import admin
from .models import Fost
# Register your models here.


class FostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','mod_date')
    list_filter = ('mod_date',)
    search_fields = ('title','content','author')




admin.site.register(Fost)