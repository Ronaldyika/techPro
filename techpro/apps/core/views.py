from django.shortcuts import render
from apps.core.models import SiteSettings, TeamMember
from apps.services.models import Service
from apps.services.views import DEFAULT_SERVICES
from apps.projects.models import Project
from apps.reviews.models import Review
from apps.blog.models import BlogPost


def home(request):
    settings_obj = SiteSettings.get_settings()
    services = Service.objects.filter(is_active=True)[:6]
    projects = Project.objects.filter(is_featured=True)[:6]
    reviews = Review.objects.filter(is_approved=True)[:6]
    recent_posts = BlogPost.objects.filter(status='published')[:3]
    context = {
        'site': settings_obj,
        'services': services,
        'projects': projects,
        'reviews': reviews,
        'recent_posts': recent_posts,
        'default_services': DEFAULT_SERVICES,
    }
    return render(request, 'core/home.html', context)


def about(request):
    settings_obj = SiteSettings.get_settings()
    team = TeamMember.objects.filter(is_active=True)
    context = {'site': settings_obj, 'team': team}
    return render(request, 'core/about.html', context)
