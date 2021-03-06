from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated, IsAdminUser

schema_view = get_schema_view(
    openapi.Info(
        title="LouisNicolle API",
        default_version='v1',
        description="API description",
    ),
    public=False,
    permission_classes=(IsAuthenticated, IsAdminUser),
    patterns=[
        path('aeon/', include('aeon.urls')),
        path('climax_tracker/', include('climax_tracker.urls')),
        path('achievement/', include('achievement.urls')),
        path('stats/', include('stats.urls')),
    ],
)

urlpatterns = [
    path('', include('louis_nicolle.url')),
    path('admin/', admin.site.urls),
    path('aeon/', include('aeon.urls')),
    path('climax_tracker/', include('climax_tracker.urls')),
    path('achievement/', include('achievement.urls')),
    path('stats/', include('stats.urls')),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
