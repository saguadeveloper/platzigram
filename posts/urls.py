# Django
from django.urls import path

from . import views

urlpatterns = [
    path(
        route='',
        view=views.PostFeedView.as_view(),
        name='feed'
    ),

    path(
        route='<int:post_id>',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='new',
        view=views.CreatePostView.as_view(),
        name='new_posts'
    ),
]