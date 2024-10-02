from django.db import models
from datetime import date
from cloudinary.models import CloudinaryField
from home.models import Consultant
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE,
        related_name="consultant_projects"
        )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    sub_heading = models.CharField(max_length=250, blank=True)
    summary = models.TextField(blank=True)
    project_image = CloudinaryField('image', default='placeholder')
    image_alt_text = models.CharField(max_length=200, blank=True)
    detail_image = CloudinaryField('image', default='placeholder')
    detail_image_alt = models.CharField(max_length=200, blank=True)
    confidential = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    link = models.URLField(max_length=250, blank=True)
    link_text = models.CharField(max_length=200, blank=True)
    customer = models.CharField(max_length=250, blank=True)
    start = models.DateField(default=date.today)
    end = models.DateField(default=date.today)
    show_in_home = models.BooleanField(default=True)

    class Meta:
        ordering = ["consultant_id", "display_order"]

    def __str__(self):
        return f"{self.consultant_id} | {self.title}"


class Client(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client_access"
        )
    allow_delete = models.BooleanField()
    consultant = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="client_access",
        default=1
        )
    email = models.EmailField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    approval_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["client", "approval_date"]

    def __str__(self):
        return f"{self.client} | {self.email} | {self.approved}"


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
    heading_1 = models.CharField(max_length=200, blank=True)
    heading_2 = models.CharField(max_length=200, blank=True)
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
    alt_text = models.CharField(max_length=200, default='placeholder')
    image_caption_heading = models.CharField(max_length=250, blank=True,
                                             default='Caption Heading')
    image_caption_text = models.CharField(max_length=250,  blank=True,
                                          default='Caption Text')
    image_caption_mode = models.CharField(max_length=100,  blank=True,
                                          default='light')
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["section_id", "display_order"]

    def __str__(self):
        return f"{self.section} | {self.alt_text} | {self.display_order}"


class SectionVideo(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_videos"
        )
    video = CloudinaryField('video', resource_type='video',
                            default='placeholder')
    video_alt_text = models.CharField(max_length=200, default='placeholder')
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["section_id", "display_order"]

    def __str__(self):
        return f"{self.section} | {self.video_alt_text} | {self.display_order}"


class SectionURLS(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_urls"
        )
    link = models.URLField(max_length=250, blank=False)
    link_text = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["section_id", "display_order"]

    def __str__(self):
        return f"{self.section_id} | {self.alt_text}"
