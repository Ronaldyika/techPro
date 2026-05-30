from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'inquiries', views.InquiryViewSet, basename='inquiry')

urlpatterns = router.urls
