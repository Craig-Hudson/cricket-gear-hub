from django import forms
from .models import StaffMember


class AddStaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = [
            'first_name', 'last_name', 'job_title', 'bio', 'profile_picture'
            ]


class EditStaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = [
            'first_name', 'last_name', 'job_title', 'bio', 'profile_picture'
            ]
