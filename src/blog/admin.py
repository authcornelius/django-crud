from calendar import c
from django.contrib import admin
from .models import Post


# Register your models here.
class PostDB(admin.ModelAdmin):
    list_display = [
        "title", "slug", "author", "body", "publish",
        "created", "updated", "status"
    ]
