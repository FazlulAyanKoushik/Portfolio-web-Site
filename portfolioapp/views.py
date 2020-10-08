from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here.
def about_me(request, name):
    profile = Profile.objects.get(user__username = name)
    about = AboutMe.objects.get(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'about': about, 'profile': profile, 'contact':contact}
    return render(request, 'about_me.html', context)

def home(request, name):
    profile = Profile.objects.get(user__username = name)
    home = Home.objects.get(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'home':home, 'profile': profile, 'contact':contact}
    return render(request, 'home.html',context)

def experience(request, name):
    profile = Profile.objects.get(user__username = name)
    experience = Experience.objects.filter(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'experience': experience, 'profile': profile, 'contact':contact}
    return render(request, 'experience.html', context)

def education(request, name):
    profile = Profile.objects.get(user__username = name)
    education = Education.objects.filter(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'education':education, 'profile': profile, 'contact':contact}
    return render(request, 'education.html', context)

def skill(request,name):
    profile = Profile.objects.get(user__username = name)
    skill = Skill.objects.filter(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'skill':skill, 'profile': profile, 'contact':contact}
    return render(request, 'skill.html',context)

def interest(request,name):
    profile = Profile.objects.get(user__username = name)
    interest = Interest.objects.filter(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'interest':interest, 'profile': profile, 'contact':contact}
    return render(request, 'interest.html',context)

def award(request,name):
    profile = Profile.objects.get(user__username = name)
    award = Award.objects.filter(user__username = name)
    contact = Contact.objects.get(user__username = name)
    context = {'award':award, 'profile': profile, 'contact':contact}
    return render(request, 'award.html',context)        

#Custom Admin Views

def c_admin_home(request):
    profile = Profile.objects.get(user = request.user)
    context = {'profile': profile}
    return render(request, 'c_admin_home.html', context)

def c_about_me(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = AboutMeForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = AboutMeForm
            context = {'form': form, 'profile': profile}
            return render(request, 'c_about_me.html', context)
    else:
        form = AboutMeForm
        context = {'form': form, 'profile': profile}
        return render(request, 'c_about_me.html', context)

def c_education(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = EducationForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_education.html', context)
    else:
        form = EducationForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_education.html', context)

def c_skill(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = SkillForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_skill.html', context)
    else:
        form = SkillForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_skill.html', context)

def c_experience(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = ExperienceForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_experience.html', context)
    else:
        form = ExperienceForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_experience.html', context)

def c_interest(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = InterestForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_interest.html', context)
    else:
        form = InterestForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_interest.html', context)

def c_award(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = AwardForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = AwardForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_award.html', context)
    else:
        form = AwardForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_award.html', context)

def c_contact(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = ContactForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_contact.html', context)
    else:
        form = ContactForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_contact.html', context)

def c_profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            form = ProfileForm()
            context = {'form':form, 'profile': profile}
            return render(request, 'c_profile.html', context)
    else:
        form = ProfileForm()
        context = {'form':form, 'profile': profile}
        return render(request, 'c_profile.html', context)

def c_edit_list_education(request):
    profile = Profile.objects.get(user = request.user)
    education = Education.objects.filter(user = request.user)
    context = {'education': education, 'profile': profile}
    return render(request, 'c_edit_list_education.html', context)

def c_edit_education(request, id):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        pi = Education.objects.get(pk = id)
        form = EducationForm(request.POST, instance = pi)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('/c-edit-list-education')
    else:        
        pi = Education.objects.get(pk = id)
        form = EducationForm(instance = pi)
        context = {'form': form, 'profile': profile} 
        return render(request,'c_edit_education.html', context)

def c_delete_education(request, id):
    education = Education.objects.get(id = id)
    education.delete()
    return redirect('/c-edit-list-education')

def c_edit_list_skill(request):
    profile = Profile.objects.get(user = request.user)
    skill = Skill.objects.filter(user = request.user)
    context = {'skill': skill, 'profile': profile}
    return render(request, 'c_edit_list_skill.html', context)

def c_edit_skill(request, id):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        pi = Skill.objects.get(pk = id)
        form = SkillForm(request.POST, instance = pi)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('/c-edit-list-skill')
    else:        
        pi = Skill.objects.get(pk = id)
        form = SkillForm(instance = pi)
        context = {'form': form, 'profile': profile} 
        return render(request,'c_edit_skill.html', context)

def c_delete_skill(request, id):
    skill = Skill.objects.get(id = id)
    skill.delete()
    return redirect('/c-edit-list-skill')

def c_edit_list_experience(request):
    profile = Profile.objects.get(user = request.user)
    experience = Experience.objects.filter(user = request.user)
    context = {'experience': experience, 'profile': profile}
    return render(request, 'c_edit_list_experience.html', context)

def c_edit_experience(request, id):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        pi = Experience.objects.get(pk = id)
        form = ExperienceForm(request.POST, instance = pi)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('/c-edit-list-experience')
    else:        
        pi = Experience.objects.get(pk = id)
        form = ExperienceForm(instance = pi)
        context = {'form': form, 'profile': profile} 
        return render(request,'c_edit_experience.html', context)

def c_delete_experience(request, id):
    experience = Experience.objects.get(id = id)
    experience.delete()
    return redirect('/c-edit-list-experience')

def c_edit_list_interest(request):
    profile = Profile.objects.get(user = request.user)
    interest = Interest.objects.filter(user = request.user)
    context = {'interest': interest, 'profile': profile}
    return render(request, 'c_edit_list_interest.html', context)

def c_edit_interest(request, id):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        pi = Interest.objects.get(pk = id)
        form = InterestForm(request.POST, instance = pi)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('/c-edit-list-interest')
    else:        
        pi = Interest.objects.get(pk = id)
        form = InterestForm(instance = pi)
        context = {'form': form, 'profile': profile} 
        return render(request,'c_edit_interest.html', context)

def c_delete_interest(request, id):
    interest = Interest.objects.get(id = id)
    interest.delete()
    return redirect('/c-edit-list-interest')


def c_edit_list_award(request):
    profile = Profile.objects.get(user = request.user)
    award = Award.objects.filter(user = request.user)
    context = {'award': award, 'profile': profile}
    return render(request, 'c_edit_list_award.html', context)

def c_edit_award(request, id):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        pi = Award.objects.get(pk = id)
        form = AwardForm(request.POST, instance = pi)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('/c-edit-list-award')
    else:        
        pi = Award.objects.get(pk = id)
        form = AwardForm(instance = pi)
        context = {'form': form, 'profile': profile} 
        return render(request,'c_edit_award.html', context)

def c_delete_award(request, id):
    award = Award.objects.get(id = id)
    award.delete()
    return redirect('/c-edit-list-award')
