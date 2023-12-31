from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Post)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)