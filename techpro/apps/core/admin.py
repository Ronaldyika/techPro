from django.contrib import admin
from .models import SiteSettings, TeamMember


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Info', {'fields': ('company_name', 'tagline', 'email', 'phone', 'whatsapp', 'address', 'logo')}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url')}),
        ('Statistics', {'fields': ('years_experience', 'projects_completed', 'happy_clients', 'team_members')}),
        ('About', {'fields': ('about_text', 'mission_text', 'vision_text')}),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
