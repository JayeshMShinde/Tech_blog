from django.contrib import admin
from blog_app.models import Post, BlogComment


admin.site.register((Post, BlogComment))
