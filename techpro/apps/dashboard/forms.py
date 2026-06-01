from django import forms
from apps.core.models import TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = [
            'name', 'role', 'bio', 'photo', 'email', 'linkedin', 'facebook_url',
            'twitter_url', 'instagram_url', 'whatsapp_url', 'order', 'is_active'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control form-control-dark', 'rows': 4}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-dark'}),
            'role': forms.TextInput(attrs={'class': 'form-control form-control-dark'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-dark'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control form-control-dark'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control form-control-dark'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control form-control-dark'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control form-control-dark'}),
            'whatsapp_url': forms.URLInput(attrs={'class': 'form-control form-control-dark'}),
            'order': forms.NumberInput(attrs={'class': 'form-control form-control-dark'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
