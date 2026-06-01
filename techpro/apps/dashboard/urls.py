from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.dashboard_login, name='dashboard_login'),
    path('logout/', views.dashboard_logout, name='dashboard_logout'),
    path('', views.dashboard_home, name='dashboard_home'),
    path('inquiries/', views.dashboard_inquiries, name='dashboard_inquiries'),
    path('reviews/', views.dashboard_reviews, name='dashboard_reviews'),
    path('team/', views.dashboard_team, name='dashboard_team'),
    path('team/<int:member_id>/', views.dashboard_team_edit, name='dashboard_team_edit'),
    path('team/<int:member_id>/delete/', views.dashboard_team_delete, name='dashboard_team_delete'),
    path('projects/', views.dashboard_projects, name='dashboard_projects'),
    path('blog/', views.dashboard_blog, name='dashboard_blog'),
    path('services/', views.dashboard_services, name='dashboard_services'),
    path('settings/', views.dashboard_settings, name='dashboard_settings'),
    path('api/stats/', views.DashboardStatsAPI.as_view(), name='dashboard_stats_api'),
]
