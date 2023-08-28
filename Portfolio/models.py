from django.db import models
from datetime import datetime

# Create your models here.

class About(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Education(models.Model):
    date=models.CharField(max_length=100)
    degree =models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.degree

class Experience(models.Model):
    date = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    def __str__(self):
        return self.framework


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Certification(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')  # Make sure to configure your MEDIA_ROOT and MEDIA_URL settings

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_scope = models.CharField(max_length=200)
    start_date =models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    information = models.TextField()

    def __str__(self):
        return self.name




