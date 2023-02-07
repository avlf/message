from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from message_servise import settings

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('message_app.urls')),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
