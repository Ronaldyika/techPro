from django.contrib import admin
from .models import Project, ProjectCategory, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'is_featured', 'created_at']
    list_editable = ['is_featured', 'status']
    list_filter = ['category', 'status', 'is_featured']
    search_fields = ['title', 'client']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
