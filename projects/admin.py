from django.contrib import admin
from .models import (
    Project, Category, Learning, Section,
    SectionImage, Client, SectionVideo,
    SectionURL
)

# Register your models here.
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Learning)
admin.site.register(Section)
admin.site.register(SectionImage)
admin.site.register(SectionURL)
admin.site.register(SectionVideo)
