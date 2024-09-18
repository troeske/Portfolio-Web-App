from django.contrib import admin
from .models import Project, Category, Learning, Section, SectionImages

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Learning)
admin.site.register(Section)
admin.site.register(SectionImages)