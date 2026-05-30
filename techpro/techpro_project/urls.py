from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API endpoints
    path('api/services/', include('apps.services.urls')),
    path('api/projects/', include('apps.projects.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    path('api/contact/', include('apps.contact.urls')),
    path('api/blog/', include('apps.blog.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
    # CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Dashboard
    path('dashboard/', include('apps.dashboard.urls')),
    # Frontend views
    path('', include('apps.core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin customization
admin.site.site_header = 'TechPro Engineering Admin'
admin.site.site_title = 'TechPro Admin'
admin.site.index_title = 'Administration Dashboard'
