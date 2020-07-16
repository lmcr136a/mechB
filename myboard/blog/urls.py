from django.urls import path
from . import views

app_name='blog'

urlpatterns =[
    path('', views.Home, name='Home'),
    path('post/', views.PostLV, name='PostLV'),
    path('post/<int:pk>/',views.PostDV,name='PostDV'),
#    path('archive/',views.PostAV,name='PostAV'),
#    path('archive/<int:year>/',views.PostYAV,name='PostYAV'),
#    path('archive/<int:year>/<int:month>/',views.PostMAV,name='PostMAV'),
#    path('archive/<int:year>/<int:month>/<int:day>/',views.PostDAV,name='PostDAV'),
#    path('archive/today/',views.PostTAV,name='PostTAV'),
    path('post/new/',views.PostN, name='PostN'),
    path('post/<int:pk>/edit/',views.PostE, name='PostE'),
     path('delete/<int:post_id>/',views.delete, name='delete'),
]

