# Django
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)