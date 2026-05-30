from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ServiceViewSet, basename='service')
router.register(r'categories', views.ServiceCategoryViewSet, basename='service-category')

# Frontend URLs - add to core urls.py
frontend_urlpatterns = [
    path('services/', views.services_page, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
]

urlpatterns = router.urls
