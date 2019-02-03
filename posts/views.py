# Posts Views

# Django

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


# Models
from .models import Post

# Forms
from .model_form import PostForm


class PostFeedView(LoginRequiredMixin, ListView):
    template_name = 'post/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 3
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'post/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


# def new_posts(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()
#
#     return render(request, 'post/create_post.html', context={
#         'form': form,
#         'user': request.user,
#         'profile': request.user.profile
#     })