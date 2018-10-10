from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
	"""control every user have bio and pic"""
	
	def __init__(self, get_response):
		"""moddle initialization"""
		self.get_response = get_response

	def __call__(self, request):
		"""	pass """
		if not request.user.is_anonymous:
			if not request.user.is_staff:
				profile = request.user.profile
				if not profile.picture or not profile.bio:
					if request.path != reverse('users:update') and request.path != reverse('users:logout'):
						return redirect('users:update')
		
		response = self.get_response(request)

		return response