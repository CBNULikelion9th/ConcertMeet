from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','user','created_at')

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display=('message','post','user')

@admin.register(PostDeclaration)
class PostDeclarationAdmin(admin.ModelAdmin):
    list_display=('message','post','user','process')

@admin.register(CommentDeclaration)
class CommentDeclarationAdmin(admin.ModelAdmin):
    list_display=('message','post','comment','user','process')

admin.site.register(Participant)
admin.site.register(Concert)


