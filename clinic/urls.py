from rest_framework.routers import DefaultRouter

from clinic.views import ClientViewSet

clinic_router = DefaultRouter()
clinic_router.register('clients', ClientViewSet)
