from django.db import models
from datetime import date
from cloudinary.models import CloudinaryField
from home.models import Consultant

# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="consultant_projects"
        )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    sub_heading = models.CharField(max_length=250, blank=True)
    summary = models.TextField(blank=True)
    project_image = CloudinaryField('image', default='placeholder')
    confidential = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["consultant_id", "display_order"]

    def __str__(self):
       return f"{self.consultant_id} | {self.title}"


class Category(models.Model):
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="projects_categories"
        )
    category = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["project_id", "display_order"]

    def __str__(self):
       return f"{self.project_id} | {self.category}"
    
class Learning(models.Model):
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="projects_learnings"
        )
    header = models.CharField(max_length=200, unique=True)
    text = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["project_id", "display_order"]

    def __str__(self):
       return f"{self.project_id} | {self.header}"
    

class Section(models.Model):
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="projects_sections"
        )
    heading_1 = models.CharField(max_length=200, unique=True)
    heading_2 = models.CharField(max_length=200, unique=True)
    text = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    orientation_right = models.BooleanField(default=False)

    class Meta:
        ordering = ["project_id", "display_order"]

    def __str__(self):
       return f"{self.project_id} | {self.heading_1}"
    

class SectionImages(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_images"
        )
    image = CloudinaryField('image', default='placeholder')
    alt_text = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["section_id", "display_order"]

    def __str__(self):
       return f"{self.section_id} | {self.alt_text}"

class SectionURLS(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_urls"
        )
    url = models.URLField(max_length=250, blank=False)
    alt_text = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["section_id", "display_order"]

    def __str__(self):
       return f"{self.section_id} | {self.alt_text}"
    