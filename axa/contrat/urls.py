from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from contrat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('devis/', views.devis, name='devis'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
