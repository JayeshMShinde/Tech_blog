# Generated by Django 4.2.5 on 2023-10-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(blank=True, null=True),
        ),
    ]
