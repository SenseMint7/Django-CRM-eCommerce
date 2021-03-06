from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions

# drf_yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Django Admin API",
      default_version='v1',
      description="Django Admin + mongodb + ELK",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   validators=['flex'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = 'Django Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/api-doc/', include('django.contrib.admindocs.urls')),
    path('ecommerce/', include('ecommerce.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]