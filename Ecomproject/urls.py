from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')),
    path('shopapp/', include('shopapp.urls')),
    path('blogapp/', include('blogapp.urls')),
    path('contactapp/', include('contactapp.urls')),
    path('pagesapp/', include('pagesapp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)