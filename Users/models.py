"""Users models."""

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	"""docstring for Profile"models.Model
	def __init__(self, arg):
		super(Profile,models.Model).__init__()
		self.arg = arg """

	user = models.OneToOneField(User, on_delete=models.CASCADE)	
	website = models.URLField(max_length=200, blank=True)
	bio = models.TextField(blank=True)
	picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

	readonly_fields = ['user__last_login']

	def __str__(self):
		return self.user.username
		