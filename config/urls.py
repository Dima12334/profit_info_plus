from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('', include('apps.spend.api.urls')),
    path('', include('apps.revenue.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]
