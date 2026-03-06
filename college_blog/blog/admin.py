from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This displays these columns in the list view
    list_display = ['title', 'slug']
    
    # This automatically fills the slug field based on the title
    prepopulated_fields = {'slug': ('title',)}