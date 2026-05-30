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
    about_text = models.TextField(blank=True)
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
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"
