from django.conf.urls.static import static
from django.urls import path

from config import settings
from yadja.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)