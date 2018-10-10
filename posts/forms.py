from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
	"""docstring for PostForm"forms.ModelForm|"""
	class Meta:
		"""Form setting."""

		model = Post
		fields = ('user', 'profile', 'title', 'photo')