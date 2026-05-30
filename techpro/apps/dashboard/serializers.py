from rest_framework import serializers
from apps.contact.models import Inquiry
from apps.reviews.models import Review
from apps.projects.models import Project
from apps.blog.models import BlogPost


class DashboardStatsSerializer(serializers.Serializer):
    total_inquiries = serializers.IntegerField()
    new_inquiries = serializers.IntegerField()
    total_reviews = serializers.IntegerField()
    pending_reviews = serializers.IntegerField()
    total_projects = serializers.IntegerField()
    total_posts = serializers.IntegerField()
