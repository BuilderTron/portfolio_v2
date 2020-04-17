from django.db import models






# Projects

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    git_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# Resume

class Resume(models.Model):
    title = models.CharField(max_length=200, null=True)
    resumefile = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.title




# Skills
class Skill(models.Model):
    title = models.CharField(max_length=200, null=True)
    
