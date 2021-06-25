from django.contrib import admin
from .models import Post
from .models import Concert


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','user','created_at')

admin.site.register(Concert)

