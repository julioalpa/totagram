"""posts.urls"""

from django.urls import path
from posts import views

urlpatterns = [
	path(
		route = '',
		view = views.PostFeedView.as_view()
	),
	path(
		route = "posts/",
		view = views.PostFeedView.as_view(),
		name = "feed"
	),
	path(
		route = "posts/new",
		view = views.CreatePostView.as_view(),
		name = "create"
	)
	,
	path(
		route = "posts/<int:id_post>",
		view = views.PostDetailView.as_view(),
		name = "detail"
	)
]