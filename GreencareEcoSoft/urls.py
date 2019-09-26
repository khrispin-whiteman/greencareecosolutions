from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greencare.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('summernote/', include('django_summernote.urls')),
]

admin.site.site_header = 'Greencare Eco Administration'
admin.site.index_title = 'System Applications'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
