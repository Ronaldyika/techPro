from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Project, ProjectCategory, ProjectImage
from .serializers import ProjectSerializer, ProjectCategorySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ['category', 'status', 'is_featured']
    search_fields = ['title', 'description', 'client']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]


class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def projects_page(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects, 'categories': categories})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.exclude(pk=project.pk)[:3]
    return render(request, 'projects/project_detail.html', {'project': project, 'related': related})
