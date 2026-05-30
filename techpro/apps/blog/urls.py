from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.BlogCategoryViewSet, basename='blog-category')
router.register(r'', views.BlogPostViewSet, basename='blog')

urlpatterns = router.urls
