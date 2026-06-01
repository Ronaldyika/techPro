from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Avg, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.contact.models import Inquiry
from apps.reviews.models import Review
from apps.projects.models import Project
from apps.blog.models import BlogPost
from apps.services.models import Service
from apps.core.models import SiteSettings, TeamMember
from .forms import TeamMemberForm


def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions.')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')


@login_required(login_url='/dashboard/login/')
def dashboard_home(request):
    if not request.user.is_staff:
        return redirect('home')
    stats = {
        'total_team_members': TeamMember.objects.count(),
        'total_reviews': Review.objects.count(),
        'approved_reviews': Review.objects.filter(is_approved=True).count(),
        'pending_reviews': Review.objects.filter(is_approved=False).count(),
        'total_projects': Project.objects.count(),
        'total_services': Service.objects.count(),
        'avg_rating': Review.objects.filter(is_approved=True).aggregate(avg=Avg('rating'))['avg'] or 0,
    }
    recent_inquiries = Inquiry.objects.order_by('-created_at')[:5]
    pending_reviews = Review.objects.filter(is_approved=False).order_by('-created_at')[:5]
    recent_projects = Project.objects.order_by('-created_at')[:5]

    # Rating distribution for chart
    rating_dist = []
    for i in range(1, 6):
        rating_dist.append(Review.objects.filter(is_approved=True, rating=i).count())

    context = {
        'stats': stats,
        'recent_inquiries': recent_inquiries,
        'pending_reviews': pending_reviews,
        'recent_projects': recent_projects,
        'rating_dist': rating_dist,
    }
    return render(request, 'dashboard/home.html', context)


@login_required(login_url='/dashboard/login/')
def dashboard_inquiries(request):
    if not request.user.is_staff:
        return redirect('home')
    inquiries = Inquiry.objects.all().order_by('-created_at')
    return render(request, 'dashboard/inquiries.html', {'inquiries': inquiries})


@login_required(login_url='/dashboard/login/')
def dashboard_reviews(request):
    if not request.user.is_staff:
        return redirect('home')
    reviews = Review.objects.all().order_by('-created_at')
    status_filter = request.GET.get('filter')
    query = request.GET.get('q', '').strip()

    if status_filter == 'pending':
        reviews = reviews.filter(is_approved=False)
    elif status_filter == 'approved':
        reviews = reviews.filter(is_approved=True)

    if query:
        reviews = reviews.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(comment__icontains=query) |
            Q(service__icontains=query)
        )

    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        action = request.POST.get('action')
        try:
            review = Review.objects.get(pk=review_id)
            if action == 'approve':
                review.is_approved = True
                review.save()
                messages.success(request, 'Review approved.')
            elif action == 'reject':
                review.is_approved = False
                review.save()
                messages.success(request, 'Review rejected.')
            elif action == 'delete':
                review.delete()
                messages.success(request, 'Review deleted.')
        except Review.DoesNotExist:
            messages.error(request, 'Review not found.')
        return redirect('dashboard_reviews')

    return render(request, 'dashboard/reviews.html', {'reviews': reviews, 'query': query, 'status_filter': status_filter})


@login_required(login_url='/dashboard/login/')
def dashboard_team(request):
    if not request.user.is_staff:
        return redirect('home')

    query = request.GET.get('q', '').strip()
    team_members = TeamMember.objects.all().order_by('order', 'name')
    if query:
        team_members = team_members.filter(
            Q(name__icontains=query) | Q(role__icontains=query) | Q(bio__icontains=query)
        )

    form = TeamMemberForm()
    if request.method == 'POST' and request.POST.get('action') == 'create':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member added successfully.')
            return redirect('dashboard_team')
        else:
            messages.error(request, 'Please correct the errors in the team member form.')

    return render(request, 'dashboard/team.html', {
        'team_members': team_members,
        'form': form,
        'query': query,
    })


@login_required(login_url='/dashboard/login/')
def dashboard_team_edit(request, member_id):
    if not request.user.is_staff:
        return redirect('home')

    member = get_object_or_404(TeamMember, pk=member_id)
    form = TeamMemberForm(request.POST or None, request.FILES or None, instance=member)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Team member updated successfully.')
        return redirect('dashboard_team')

    return render(request, 'dashboard/team_edit.html', {
        'form': form,
        'member': member,
    })


@login_required(login_url='/dashboard/login/')
def dashboard_team_delete(request, member_id):
    if not request.user.is_staff:
        return redirect('home')

    member = get_object_or_404(TeamMember, pk=member_id)
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Team member deleted successfully.')
    return redirect('dashboard_team')


@login_required(login_url='/dashboard/login/')
def dashboard_projects(request):
    if not request.user.is_staff:
        return redirect('home')
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'dashboard/projects.html', {'projects': projects})


@login_required(login_url='/dashboard/login/')
def dashboard_blog(request):
    if not request.user.is_staff:
        return redirect('home')
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'dashboard/blog.html', {'posts': posts})


@login_required(login_url='/dashboard/login/')
def dashboard_services(request):
    if not request.user.is_staff:
        return redirect('home')
    services = Service.objects.all().order_by('order', 'name')
    return render(request, 'dashboard/services.html', {'services': services})


@login_required(login_url='/dashboard/login/')
def dashboard_settings(request):
    if not request.user.is_staff:
        return redirect('home')
    site = SiteSettings.get_settings()
    if request.method == 'POST':
        site.company_name = request.POST.get('company_name', site.company_name)
        site.tagline = request.POST.get('tagline', site.tagline)
        site.email = request.POST.get('email', site.email)
        site.phone = request.POST.get('phone', site.phone)
        site.whatsapp = request.POST.get('whatsapp', site.whatsapp)
        site.address = request.POST.get('address', site.address)
        site.hero_heading = request.POST.get('hero_heading', site.hero_heading)
        site.hero_subtitle = request.POST.get('hero_subtitle', site.hero_subtitle)
        site.hero_cta_text = request.POST.get('hero_cta_text', site.hero_cta_text)
        site.hero_cta_url = request.POST.get('hero_cta_url', site.hero_cta_url)
        site.about_heading = request.POST.get('about_heading', site.about_heading)
        site.values_intro = request.POST.get('values_intro', site.values_intro)
        site.facebook_url = request.POST.get('facebook_url', site.facebook_url)
        site.twitter_url = request.POST.get('twitter_url', site.twitter_url)
        site.linkedin_url = request.POST.get('linkedin_url', site.linkedin_url)
        site.instagram_url = request.POST.get('instagram_url', site.instagram_url)
        site.about_text = request.POST.get('about_text', site.about_text)
        site.mission_text = request.POST.get('mission_text', site.mission_text)
        site.vision_text = request.POST.get('vision_text', site.vision_text)
        site.save()
        messages.success(request, 'Site settings updated successfully.')
        return redirect('dashboard_settings')
    return render(request, 'dashboard/settings.html', {'site': site})


class DashboardStatsAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = {
            'total_inquiries': Inquiry.objects.count(),
            'new_inquiries': Inquiry.objects.filter(status='new').count(),
            'total_reviews': Review.objects.count(),
            'pending_reviews': Review.objects.filter(is_approved=False).count(),
            'total_projects': Project.objects.count(),
            'total_posts': BlogPost.objects.count(),
        }
        return Response(data)
