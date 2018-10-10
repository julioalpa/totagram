from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from Users.models import Profile

# Register your models here.

#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	
	list_display = ('user', 'website', 'bio', 'picture')
	list_display_links = ('user', 'website', 'bio')
	list_editable = ['picture']
	
	search_fields = (
		'user__email',
		'user__first_name', 
		'user__last_name', 
		'user__username', 
		'website'
		)

	list_filter = (
		'user__is_active', 
		'user__is_staff'
		)

	"""tupla, q contiene tuplas () -> {} diccionarios"""
	fieldsets = (
		('Profile', {
			'fields': (
				('user', 'picture'),				
				),
			}),		
		('Extra Info',{
			'fields': (
				('website', 'bio')
				)
		}),
		)

	readonly_fields = ['user']

class ProfileInLine(admin.StackedInline):
	
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):

	inlines = (ProfileInLine,)		
		
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
