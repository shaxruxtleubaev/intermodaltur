from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from src.settings.base import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

urlpatterns += static(MEDIA_URL, decument_root=MEDIA_ROOT)