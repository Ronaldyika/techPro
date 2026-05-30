from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'service', 'rating', 'title', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at', 'is_approved']
