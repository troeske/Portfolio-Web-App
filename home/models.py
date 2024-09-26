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
    intro_text_heading = models.CharField(max_length=200, blank=False, default="heading.")
    intro_text = models.TextField(blank=False, default="default intro text.")
    about_me = models.TextField(blank=False, default="default about me text.")
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
    proficiency = models.IntegerField(null=True, blank=True)
    text = models.TextField(blank=True)
    icon = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["consultant_id","type", "display_order"]

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
    link_text = models.CharField(max_length=250, blank=True)
    link = models.URLField(max_length=250, blank=False, default="https://www.google.com")
    logo = CloudinaryField('image', default='placeholder')
    logo_alt_text = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["consultant_id", "-start"]

    def __str__(self):
        return f"{self.consultant_id} | {self.start} | {self.company} | {self.role}"

class How(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_hows"
        )
    heading = models.CharField(max_length=200, blank=False, default="heading.")
    text = models.TextField(blank=False, default="default intro text.")
    icon = CloudinaryField('image', default='placeholder')
    display_order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.heading}"
    
class PressLink(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_presslinks"
        )
    link_text = models.CharField(max_length=250, blank=False)
    link = models.URLField(max_length=250, blank=False)

    def __str__(self):
        return f"{self.consultant_id} | {self.link_text}"

class Customer(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_customers"
        )
    link_text = models.CharField(max_length=250, blank=False)
    link = models.URLField(max_length=250, blank=False)
    logo = CloudinaryField('image', default='placeholder')
    logo_alt_text = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=False)

    class Meta:
        ordering = ["consultant_id", "name"]

    def __str__(self):
        return f"{self.consultant_id} | {self.name}"

class SocialAccount(models.Model):
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_socialaccounts"
        )
    name= models.CharField(max_length=250)
    link = models.URLField(max_length=250)
    fa_icon = models.CharField(max_length=200, blank=True)
    

class Config(models.Model):
    """
    Model for storing configuration data
    """
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="home_config"        )
    key = models.CharField(max_length=200, blank=False)
    value = models.CharField(max_length=200, blank=False)
    
    class Meta:
        ordering = ["key"]

    def __str__(self):
        return f"{self.key} | {self.value}"