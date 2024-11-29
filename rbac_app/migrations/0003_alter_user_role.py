# Generated by Django 4.2.16 on 2024-11-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac_app', '0002_user_role_alter_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('moderator', 'Moderator'), ('user', 'User')], default='user', max_length=10),
        ),
    ]
