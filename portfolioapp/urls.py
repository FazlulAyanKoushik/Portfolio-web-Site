from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<name>/', home),
    path('<name>/home',home, name='home'),
    path('<name>/about-me',about_me, name = 'about-me'),
    path('<name>/experience', experience, name= 'experience'),
    path('<name>/education', education, name= 'education'),
    path('<name>/skill', skill, name= 'skill'),
    path('<name>/interest', interest, name= 'interest'),
    path('<name>/award', award, name= 'award'),

    #admin urls
    # path('login/', auth_views.LoginView.as_view(),name='login'),
    path('c-admin-home', c_admin_home, name= 'c-admin-home'),
    path('c-profile', c_profile, name= 'c-profile'),
    path('c-about-me', c_about_me, name= 'c-about-me'),
    path('c-education', c_education, name= 'c-education'),
    path('c-skill', c_skill, name= 'c-skill'),
    path('c-experience', c_experience, name= 'c-experience'),
    path('c-interest', c_interest, name= 'c-interest'),
    path('c-award', c_award, name= 'c-award'),
    path('c-contact', c_contact, name= 'c-contact'),

    #edit
    # edit education
    path('c-edit-education/<int:id>', c_edit_education, name= 'c-edit-education'),
    path('c-edit-list-education', c_edit_list_education, name= 'c-edit-list-education'),
    path('c-delete-education/<int:id>', c_delete_education, name= 'c-delete-education'),

    # edit skill
    path('c-edit-list-skill', c_edit_list_skill, name= 'c-edit-list-skill'),
    path('c-edit-skill/<int:id>', c_edit_skill, name= 'c-edit-skill'),
    path('c-delete-skill/<int:id>', c_delete_skill, name= 'c-delete-skill'),

    #edit experience
    path('c-edit-list-experience', c_edit_list_experience, name= 'c-edit-list-experience'),
    path('c-edit-experience/<int:id>', c_edit_experience, name= 'c-edit-experience'),
    path('c-delete-experience/<int:id>', c_delete_experience, name= 'c-delete-experience'),

    #edit interest
    path('c-edit-list-interest', c_edit_list_interest, name= 'c-edit-list-interest'),
    path('c-edit-interest/<int:id>', c_edit_interest, name= 'c-edit-interest'),
    path('c-delete-interest/<int:id>', c_delete_interest, name= 'c-delete-interest'),
    
    #edit award
    path('c-edit-list-award', c_edit_list_award, name= 'c-edit-list-award'),
    path('c-edit-award/<int:id>', c_edit_award, name= 'c-edit-award'),
    path('c-delete-award/<int:id>', c_delete_award, name= 'c-delete-award'),

]