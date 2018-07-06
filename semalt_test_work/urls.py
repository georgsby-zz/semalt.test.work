from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
