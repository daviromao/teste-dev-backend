from rest_framework.routers import DefaultRouter

from clinic.views import ClientViewSet

clinic_router = DefaultRouter(trailing_slash=False)
clinic_router.register('clients', ClientViewSet)
