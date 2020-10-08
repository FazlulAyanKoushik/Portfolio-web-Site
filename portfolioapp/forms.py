from django.forms import ModelForm
from portfolioapp.models import *

class AboutMeForm(ModelForm):
    class Meta:
        model = AboutMe
        fields = ['about_me']

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ('user',)  

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ('user',)   

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('user',)    

class InterestForm(ModelForm):
    class Meta:
        model = Interest
        exclude = ('user',)    

class AwardForm(ModelForm):
    class Meta:
        model = Award
        exclude = ('user',)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('user',)    

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)         

 