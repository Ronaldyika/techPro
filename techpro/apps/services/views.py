from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceCategorySerializer

DEFAULT_SERVICES = [
    {
        'name': 'Solar Installation',
        'short_description': 'Complete solar energy systems for homes and businesses. Grid-tied, off-grid, and hybrid solutions with quality panels and batteries.',
        'icon': 'bi-sun-fill',
    },
    {
        'name': 'Electrical Wiring',
        'short_description': 'Safe and code-compliant residential and commercial electrical wiring by certified electricians.',
        'icon': 'bi-plug-fill',
    },
    {
        'name': 'CCTV Security',
        'short_description': 'Full CCTV surveillance system design, supply, installation, and maintenance for homes and businesses.',
        'icon': 'bi-camera-video-fill',
    },
    {
        'name': 'Wireless Networks',
        'short_description': 'Enterprise-grade wireless network design and deployment. Fast, secure, and scalable for any environment.',
        'icon': 'bi-wifi',
    },
    {
        'name': 'Smart Home',
        'short_description': 'Smart lighting, automated security, climate control, and integrated IoT systems for modern living.',
        'icon': 'bi-house-gear-fill',
    },
    {
        'name': 'Industrial Electrical',
        'short_description': 'High-capacity industrial electrical systems, motor controls, panel boards, and industrial automation.',
        'icon': 'bi-lightning-charge-fill',
    },
]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category', 'is_featured']
    search_fields = ['name', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def services_page(request):
    services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects.all()
    return render(request, 'services/services.html', {'services': services, 'categories': categories, 'default_services': DEFAULT_SERVICES})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related = Service.objects.filter(is_active=True).exclude(pk=service.pk)[:3]
    return render(request, 'services/service_detail.html', {'service': service, 'related': related})
