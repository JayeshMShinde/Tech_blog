# Generated by Django 4.2.5 on 2023-10-04 05:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0004_rename_blogcomments_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_User',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
