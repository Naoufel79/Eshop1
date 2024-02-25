from django.contrib import admin
from django.urls import path  , include, re_path
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
    #path('djga/', include('google_analytics.urls')),
    #re_path(r'^djga/', include('google_analytics.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
