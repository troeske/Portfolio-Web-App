# Generated by Django 4.2.16 on 2024-09-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_client_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user_id',
        ),
        migrations.AddField(
            model_name='client',
            name='allow_delete',
            field=models.BooleanField(default=False),
        ),
    ]
