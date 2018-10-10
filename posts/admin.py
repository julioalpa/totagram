from django.contrib import admin
from posts.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	
	list_display = ('user', 'profile','title')
