from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    VATnumber = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    office_time = models.CharField(max_length=100, null=True, blank=True)
    blochure = models.FileField(upload_to='brochures/', null=True, blank=True)

    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    pinterest = models.CharField(max_length=200, null=True, blank=True)
    vimo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.email} - {self.phone}"


class TestimonialInfo(models.Model):
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_position = models.CharField(max_length=255, null=True, blank=True)
    client_image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    quote = models.TextField()

    def __str__(self):
        return self.client_name if self.client_name else "Unnamed Client"
    
from django.db import models

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class OurProjects(models.Model):
    project_image = models.ImageField(upload_to='projects/', null=True, blank=True)
    project_count = models.CharField(max_length=10, null=True, blank=True)
    project_title = models.CharField(max_length=255, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    ChallangeAndSolutionTitle = models.CharField(max_length=255, null=True, blank=True)
    ChallangeAndSolution_description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    timeline = models.CharField(max_length=50, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    

    def __str__(self):
        return self.project_title if self.project_title else "Unnamed Project"
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_two = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    subdescription = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=100)
    dailyquote = models.TextField(blank=True, null=True)
    quoteAuthor = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Partner(models.Model):
    image = models.ImageField(upload_to='partners/', null=True, blank=True)
    alt_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.alt_text if self.alt_text else "Unnamed Partner"
    
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100, blank=False, null=False) 
    member_category = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    pinterest = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    


