from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .forms import EditStaffMemberForm, AddStaffMemberForm
from .models import StaffMember


def staff_members(request):
    """render the staff member template and display staff members on page"""

    staff_members = StaffMember.objects.all()
    template = 'staff_members/staff_members.html'
    return render(request, template, {'staff_members': staff_members})


def add_staff_member(request):
    """add staff members to database"""

    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only store owners can add staff members'
                       )
        return redirect('login')

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
    """Edit staff members"""

    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only store owners can edit staff members'
                       )
        return redirect('login')

    staff_member = get_object_or_404(StaffMember,
                                     pk=staff_member_id)
    if request.method == 'POST':
        form = EditStaffMemberForm(request.POST,
                                   request.FILES, instance=staff_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member updated successfully.')
            return redirect(reverse('staff_members'))
    else:
        form = EditStaffMemberForm(instance=staff_member)

    template = 'staff_members/edit_staff_member.html'

    return render(request, template, {'form': form, 'staff_member': staff_member})


def delete_staff_member(request, staff_member_id):
    """Delete staff members from database"""

    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only store owners can delete staff members'
                       )
        return redirect(reverse('login'))

    staff_member = get_object_or_404(StaffMember, pk=staff_member_id)
    staff_member.delete()
    messages.success(request, 'Staff member deleted successfully.')
    return redirect(reverse('staff_members'))
