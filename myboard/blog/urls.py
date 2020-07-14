from django.urls import path
from . import views

app_name='blog'

urlpatterns =[
    path('', views.PostLV, name='post_list'),
    path('post/', views.PostLV, name='post_list'),
    path('post/<int:pk>/',views.PostDV,name='PostDV'),
    path('archive/',views.PostAV,name='post_archive'),
    path('archive/<int:year>/',views.PostYAV,name='post_year_archive'),
    path('archive/<int:year>/<int:month>/',views.PostMAV,name='post_month_archive'),
    path('archive/<int:year>/<int:month>/<int:day>/',views.PostDAV,name='post_day_archive'),
    path('archive/today/',views.PostTAV,name='post_today'),
    path('post/new/',views.PostN, name='PostN'),
    path('post/<int:pk>/edit/',views.PostE, name='PostE')

]

