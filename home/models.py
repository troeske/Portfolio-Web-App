from django.db import models
from datetime import date
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
TYPE = ((1, "Skill"), (2, "Tool"), (3, "Interest"), (4, "Role"))


class Consultant(models.Model):
    consultant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(null=True, blank=True)
    intro_text = models.TextField(blank=False, default="default intro text.")
    profile_image = CloudinaryField('image', default='placeholder')
    phone = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_skills"
        )
    label = models.CharField(max_length=200, blank=False)
    type = models.IntegerField(choices=TYPE, default=1)
    proficiency = models.IntegerField()
    text = models.TextField(blank=True)

    class Meta:
        ordering = ["consultant_id","type"]

    def __str__(self):
        return f"{self.consultant_id} | Type: {self.type} - {self.label}"


class PastEmployment(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_pastemployments"
        )
    company = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    start = models.DateField(default=date.today)
    end = models.DateField(default=date.today)
    role = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)

    class Meta:
        ordering = ["consultant_id", "-start"]

    def __str__(self):
        return f"{self.consultant_id} | {self.start} | {self.company} | {self.role}"


class PressLink(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_presslinks"
        )
    link_text = models.CharField(max_length=250, blank=False)
    link = models.URLField(max_length=250, blank=False)

    def __str__(self):
        return f"{self.consultant_id} | {self.link_text}"


class Config(models.Model):
    """
    Model for storing configuration data
    """
    key = models.CharField(max_length=200, blank=False)
    value = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.key} | {self.value}"