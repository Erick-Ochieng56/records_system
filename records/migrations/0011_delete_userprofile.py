# Generated by Django 5.1 on 2024-09-09 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_alter_user_user_permissions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]