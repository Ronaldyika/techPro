from django.urls import path
from . import views
from apps.services.views import services_page, service_detail
from apps.projects.views import projects_page, project_detail
from apps.reviews.views import reviews_page
from apps.blog.views import blog_page, blog_detail
from apps.contact.views import contact_page

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', services_page, name='services'),
    path('services/<slug:slug>/', service_detail, name='service_detail'),
    path('projects/', projects_page, name='projects'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
    path('reviews/', reviews_page, name='reviews'),
    path('blog/', blog_page, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('contact/', contact_page, name='contact'),
]
