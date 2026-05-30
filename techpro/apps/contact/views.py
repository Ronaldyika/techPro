from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Inquiry
from .serializers import InquirySerializer


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inquiry = serializer.save()
        try:
            send_mail(
                f"New Inquiry: {inquiry.subject}",
                f"From: {inquiry.name}\nEmail: {inquiry.email}\nPhone: {inquiry.phone}\n\n{inquiry.message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.COMPANY_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass
        return Response({'success': True, 'message': 'Thank you! We will get back to you shortly.'}, status=status.HTTP_201_CREATED)


def contact_page(request):
    return render(request, 'contact/contact.html')
