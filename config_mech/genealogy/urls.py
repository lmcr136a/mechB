from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'genealogy'

urlpatterns = [
    path('', views.genealogy_list, name='genealogy_list'),
    path('<int:pk>/', views.genealogy_detail, name='genealogy_detail'),
    path('new/', views.upload_genealogy, name='upload_genealogy'),
    path('<int:pk>/edit/', views.edit_genealogy, name='edit_genealogy'),
    path('delete/<int:genealogy_id>', views.delete_genealogy, name='delete_genealogy'),
    path('download/<int:pk>', views.download_genealogy, name="download_genealogy"),
]+static(settings.GENEALOGY_URL, document_root=settings.GENEALOGY_ROOT)
