from django.contrib import admin
from .models import Post
from .models import Concert
from .models import Declaration


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','user','created_at')

@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
    list_display=('message','post','user','process')

admin.site.register(Concert)


