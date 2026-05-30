from django.conf import settings
from .models import SiteSettings


def site_settings(request):
    site = SiteSettings.get_settings()
    return {
        'COMPANY_WHATSAPP': site.whatsapp or getattr(settings, 'COMPANY_WHATSAPP', '+237690000000'),
        'COMPANY_EMAIL': site.email or getattr(settings, 'COMPANY_EMAIL', 'info@techpro.com'),
        'COMPANY_PHONE': site.phone or getattr(settings, 'COMPANY_PHONE', '+237690000000'),
        'COMPANY_ADDRESS': site.address or getattr(settings, 'COMPANY_ADDRESS', 'Bamenda, Cameroon'),
        'COMPANY_FACEBOOK': site.facebook_url,
        'COMPANY_INSTAGRAM': site.instagram_url,
        'COMPANY_LINKEDIN': site.linkedin_url,
        'COMPANY_TWITTER': site.twitter_url,
    }
