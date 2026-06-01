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
        'image_url': 'images/solar_installation.jpg',
    },
    {
        'name': 'Electrical Wiring',
        'short_description': 'Safe and code-compliant residential and commercial electrical wiring by certified electricians.',
        'icon': 'bi-plug-fill',
        'image_url': 'images/electrical_wiring.jpg',
    },
    {
        'name': 'Rod Construction',
        'short_description': 'Contract rod construction and reinforcement work for foundations, columns, and structural supports.',
        'icon': 'bi-hammer',
        'image_url': 'images/rod_construction.jpg',
    },
    {
        'name': 'CCTV Security',
        'short_description': 'Full CCTV surveillance system design, supply, installation, and maintenance for homes and businesses.',
        'icon': 'bi-camera-video-fill',
        'image_url': 'images/CCTV_camera.jpg',
    },
    {
        'name': 'Smart Home',
        'short_description': 'Smart lighting, automated security, climate control, and integrated IoT systems for modern living.',
        'icon': 'bi-house-gear-fill',
        'image_url': 'images/smart_home.jpg',
    },
]

SERVICE_IMAGE_URLS = {
    'Solar Installation': 'images/solar_installation.jpg',
    'Electrical Wiring': 'images/electrical_wiring.jpg',
    'Rod Construction': 'images/rod_construction.jpg',
    'CCTV Security': 'images/CCTV_camera.jpg',
    'Smart Home': 'images/smart_home.jpg',
}


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
    excluded_services = ['Wireless Networks', 'Industrial Electrical']
    services = list(Service.objects.filter(is_active=True).exclude(name__in=excluded_services))
    for service in services:
        if service.image:
            service.display_image = service.image.url
            service.display_image_static = False
        else:
            service.display_image = SERVICE_IMAGE_URLS.get(service.name)
            service.display_image_static = True
    categories = ServiceCategory.objects.all()
    return render(request, 'services/services.html', {'services': services, 'categories': categories, 'default_services': DEFAULT_SERVICES})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related = Service.objects.filter(is_active=True).exclude(pk=service.pk)[:3]
    return render(request, 'services/service_detail.html', {'service': service, 'related': related})
