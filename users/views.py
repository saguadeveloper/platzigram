# Django

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views

from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Models
from posts.models import Post
from users.models import Profile

# Forms
from users.form import SignupForm

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.LoginView):
    template_name = 'user/login.html'
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'user/login.html', {'error': 'Invalid username and password'})
#     return render(request, 'user/login.html')


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')


class SignupView(FormView):
    template_name = "user/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form .save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()
#     return render(request, 'user/signup.html', context={
#         'form': form
#     })


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     profile = request.user.profile
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()
#
#             url = reverse('users:update_profile')
#             return redirect(url)
#
#     else:
#         form = ProfileForm()
#
#     return render(
#         request=request,
#         template_name='user/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )