# Generated by Django 4.2.5 on 2023-10-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
