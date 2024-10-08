# Generated by Django 4.2.16 on 2024-09-18 11:10

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0007_alter_skill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('summary', models.TextField(blank=True)),
                ('project_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('confidential', models.BooleanField(default=True)),
                ('display_order', models.IntegerField(default=0)),
                ('consultant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultant_projects', to='home.consultant')),
            ],
            options={
                'ordering': ['consultant_id', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_1', models.CharField(max_length=200, unique=True)),
                ('heading_2', models.CharField(max_length=200, unique=True)),
                ('text', models.TextField(blank=True)),
                ('display_order', models.IntegerField(default=0)),
                ('orientation_right', models.BooleanField(default=False)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_sections', to='projects.project')),
            ],
            options={
                'ordering': ['project_id', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200, unique=True)),
                ('text', models.TextField(blank=True)),
                ('display_order', models.IntegerField(default=0)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_learnings', to='projects.project')),
            ],
            options={
                'ordering': ['project_id', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200)),
                ('display_order', models.IntegerField(default=0)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_categories', to='projects.project')),
            ],
            options={
                'ordering': ['project_id', 'display_order'],
            },
        ),
    ]
