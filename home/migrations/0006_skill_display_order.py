# Generated by Django 4.2.16 on 2024-09-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_skill_proficiency'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
    ]
