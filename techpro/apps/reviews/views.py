from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django.db.models import Avg, Count
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.filter(is_approved=True)
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(is_approved=False)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        stats = Review.objects.filter(is_approved=True).aggregate(
            avg_rating=Avg('rating'),
            total=Count('id')
        )
        rating_dist = {}
        for i in range(1, 6):
            rating_dist[str(i)] = Review.objects.filter(is_approved=True, rating=i).count()
        return Response({**stats, 'distribution': rating_dist})


def reviews_page(request):
    reviews = Review.objects.filter(is_approved=True)
    return render(request, 'reviews/reviews.html', {'reviews': reviews})
