from django.db import models


class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200, default='TechPro Engineering')
    tagline = models.CharField(max_length=300, default='Powering the Future with Precision Engineering')
    email = models.EmailField(default='info@techpro.com')
    phone = models.CharField(max_length=30, default='+237690000000')
    whatsapp = models.CharField(max_length=30, default='+237690000000')
    address = models.TextField(default='Bamenda, Cameroon')
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=10)
    projects_completed = models.PositiveIntegerField(default=500)
    happy_clients = models.PositiveIntegerField(default=300)
    team_members = models.PositiveIntegerField(default=25)
    hero_heading = models.CharField(max_length=255, default='Reliable Engineering and Solar Energy')
    hero_subtitle = models.CharField(max_length=350, default='We are a Bamenda-based engineering and electrical solutions company committed to delivering reliable, high-quality, and innovative services. Through professionalism, technical expertise, and customer-centered solutions, we continue to build trust and satisfaction while growing our presence across the region.')
    hero_cta_text = models.CharField(max_length=120, default='Request a Free Quote')
    hero_cta_url = models.CharField(max_length=255, default='/contact/')
    about_text = models.TextField(blank=True, default='We deliver reliable solar, electrical, security, and construction support solutions from our Bamenda base.')
    about_heading = models.CharField(max_length=200, default='Building Reliable Energy and Electrical Infrastructure')
    values_intro = models.TextField(blank=True, default='Our values reflect our promise to deliver reliable solutions, professional workmanship, and customer-focused outcomes on every project.')
    mission_text = models.TextField(blank=True)
    vision_text = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"


class HomepageBanner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=350, blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=120, default='Request a Quote')
    button_url = models.CharField(max_length=255, default='/contact/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Homepage Banner'
        verbose_name_plural = 'Homepage Banners'

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, default='bi-patch-check-fill')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Core Value'
        verbose_name_plural = 'Core Values'

    def __str__(self):
        return self.title
