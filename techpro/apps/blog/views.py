from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import BlogPost, BlogCategory
from .serializers import BlogPostSerializer, BlogCategorySerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostSerializer
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'content', 'tags']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def blog_page(request):
    posts = BlogPost.objects.filter(status='published')
    categories = BlogCategory.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts, 'categories': categories})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.views += 1
    post.save(update_fields=['views'])
    related = BlogPost.objects.filter(status='published', category=post.category).exclude(pk=post.pk)[:3]
    return render(request, 'blog/blog_detail.html', {'post': post, 'related': related})
