# Generated by Django 4.2.16 on 2024-09-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
