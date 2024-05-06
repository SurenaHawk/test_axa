from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from contrat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('devis/', views.devis, name='devis'),
    path('download_pdf/', views.download_pdf, name="download_pdf"),
    path('download_docx/', views.download_docx, name="download_docx")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
