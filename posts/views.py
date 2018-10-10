"""[summary]

[description]
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

#from Totagram
from posts.forms import PostForm
from posts.models import Post

class PostFeedView(LoginRequiredMixin, ListView):
	"""docstring for PostFeedView"""
	template_name = 'posts/feed.html'
	model = Post
	ordering = ('-created',)
	paginate_by = 2
	context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
	"""docstring for PostDetailView"""
	template_name = 'posts/detail.html'
	slug_field = 'id'
	slug_url_kwarg = 'id_post'
	queryset = Post.objects.all()
	context_object_name = 'post'
		
class CreatePostView(LoginRequiredMixin, CreateView):
	"""docstring for CreatePostView"""
	template_name = 'posts/new.html'	
	form_class = PostForm
	success_url = reverse_lazy('posts:feed')

	def get_context_data(self, **kwargs):
		"""[summary]
		
		[description]
		
		Arguments:
			**kwargs {[type]} -- [description]
		"""
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context