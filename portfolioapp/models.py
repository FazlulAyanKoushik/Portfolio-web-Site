from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Home(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    image = models.ImageField()

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete = models.CASCADE)
    about_me = models.TextField()

    def __str__(self):
        return self.about_me

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length = 50)
    from_date = models.DateField()
    to_date = models.DateField()
    designation = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.company_name

class Education(models.Model):
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    institution_name = models.CharField(max_length = 50)
    name_of_degree = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50, blank = True, null = True)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.name_of_degree

class Skill(models.Model):
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title      

class Interest(models.Model):
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    title =  models.CharField(max_length = 50)       

    def __str__(self):
        return self.title

class Award(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 50)       

    def __str__(self):
        return self.title

class Contact(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete = models.CASCADE)
    address = models.TextField()
    email = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length=12)
    facebook = models.CharField(max_length = 250, blank = True, null = True)
    instagram = models.CharField(max_length = 250, blank = True, null = True)
    linkedin = models.CharField(max_length = 250, blank = True, null = True)
    github = models.CharField(max_length = 250, blank = True, null = True)

    def __str__(self):
        return self.email
