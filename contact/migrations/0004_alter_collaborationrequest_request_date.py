# Generated by Django 4.2.16 on 2024-09-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_collaborationrequest_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborationrequest',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
