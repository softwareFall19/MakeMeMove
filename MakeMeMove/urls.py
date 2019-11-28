
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('webpages.urls')),
    path('homes/', include('homes.urls')),
    path('renters/', include('renters.urls')),
    path('contacts/', include('contacts.urls')),
    path('userprofiles/', include('userprofiles.urls')),
    path('agents', include('agents.urls')),
    path('advertising', include('advertising.urls')),
    path('admin/', admin.site.urls),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

