from django.contrib import admin
from .models import Consultant, Skill, PastEmployment, PressLink, Config

# Register your models here.
admin.site.register(Consultant)
admin.site.register(Skill)
admin.site.register(PastEmployment)
admin.site.register(PressLink)
admin.site.register(Config)