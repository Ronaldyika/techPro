from django.contrib import admin
from .models import SiteSettings, TeamMember, HomepageBanner, CoreValue


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Info', {'fields': ('company_name', 'tagline', 'email', 'phone', 'whatsapp', 'address', 'logo')}),
        ('Homepage Content', {'fields': ('hero_heading', 'hero_subtitle', 'hero_cta_text', 'hero_cta_url', 'about_heading', 'about_text', 'values_intro')}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url')}),
        ('Statistics', {'fields': ('years_experience', 'projects_completed', 'happy_clients', 'team_members')}),
        ('About', {'fields': ('mission_text', 'vision_text')}),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'role', 'bio']


@admin.register(HomepageBanner)
class HomepageBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']
