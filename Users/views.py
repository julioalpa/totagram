from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from Users.forms import SignupForm
from posts.models import Post
from Users.models import Profile

class UserDetailView(LoginRequiredMixin, DetailView):		
	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'

	def get_context_data(self, **kwargs):
		"""pass"""
		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user = user).order_by('-created')

		return context

class SignupView(FormView):
	template_name = 'users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		"""[summary]
		
		[description]
		
		Arguments:
			form {[type]} -- [description]
		"""
		form.save()
		return super().form_valid(form)

# def login_view(request):
#	"""login de users""" 
#	if request.method == 'POST':
#		username = request.POST['username']
#		password = request.POST['password']
#		
#		user = authenticate(request, username=username, password=password)
#		if user:
#			login(request, user)
#			return redirect('posts:feed')
#		else:
#			return render(request, "users/login.html", {'error':'Usuario o contraseña inválidos'})
#
#	return render(request, "users/login.html")

# def signup(request):
#	if request.method == 'POST':
#		form = SignupForm(request.POST)
#		if form.is_valid():
#			form.save()
#			return redirect('users:login')
#	else:
#		form = SignupForm()
#
#	return render(
#		request = request,
#		template_name = 'users/signup.html',
#		context = {'form': form}
#		)

class UpdateDetailView(LoginRequiredMixin, UpdateView):
	"""[summary]
	
	[description]
	
	Extends:
		LoginRequiredMixin
		UpdateView
	"""
	template_name = 'users/update_profile.html'
	model = Profile
	fields = ['website','bio','picture']

	def get_object(self):
		"""[summary]
		
		[description]
		"""
		return self.request.user.profile

	def get_success_url(self):
		"""[summary]
		
		[description]
		"""
		username = self.object.user.username
		return reverse('users:detail', kwargs={'username':username})

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
	"""docstring for LogoutView"""
	template_name='users/loged_out.html'
		
class LoginView(auth_views.LoginView):
	"""docstring for LoginView"""
	template_name = 'users/login.html'