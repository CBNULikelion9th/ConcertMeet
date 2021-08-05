from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','user','created_at')

admin.site.register(Participant)

admin.site.register(Comment)

admin.site.register(Concert)

