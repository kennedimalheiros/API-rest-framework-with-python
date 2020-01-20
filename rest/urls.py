from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from agenda.views import AgendaViewSet

router = routers.DefaultRouter()
router.register(r'agenda', AgendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
