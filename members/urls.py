from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('all_members/', views.all_members, name='all_members'),
    path('add_member/', views.add_member, name='add_member'),
    path('all_members/detail/<int:id>', views.detail, name='detail'),
]
