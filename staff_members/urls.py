from django.urls import path
from . import views


urlpatterns = [
    path('', views.staff_members, name='staff_members'),
    path('add_staff_member/', views.add_staff_member, name='add_staff_member'),
    path('edit_staff_member/<int:staff_member_id>/', views.edit_staff_member, name='edit_staff_member'),
    path('delete_staff_member/<int:staff_member_id>/', views.delete_staff_member, name='delete_staff_member'),
]
