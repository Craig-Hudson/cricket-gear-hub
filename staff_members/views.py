from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EditStaffMemberForm, AddStaffMemberForm
from .models import StaffMember

def staff_members(request):
    staff_members = StaffMember.objects.all()
    template = 'staff_members/staff_members.html'
    return render(request, template, {'staff_members': staff_members})

def add_staff_member(request):
    if request.method == 'POST':
        form = AddStaffMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member added successfully.')
            return redirect('staff_members')
    else:
        form = AddStaffMemberForm()

    template = 'staff_members/add_staff_member.html'
    return render(request, template, {'form': form})

def edit_staff_member(request, staff_member_id):
    staff_member = get_object_or_404(StaffMember, pk=staff_member_id)
    if request.method == 'POST':
        form = EditStaffMemberForm(request.POST, request.FILES, instance=staff_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member updated successfully.')
            return redirect('staff_members')
    else:
        form = EditStaffMemberForm(instance=staff_member)

    template = 'staff_members/edit_staff_member.html'

    return render(request, template, {'form': form})

def delete_staff_member(request, staff_member_id):
    staff_member = get_object_or_404(StaffMember, pk=staff_member_id)
    staff_member.delete()
    messages.success(request, 'Staff member deleted successfully.')
    return redirect('staff_members')
