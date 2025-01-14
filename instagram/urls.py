"""
URL configuration for instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns

from posts.views import PostCreateView, PostDetailView, like_post, like_post_ajax

from .views import AboutView, ContactView, HomeView, LegalView, LoginView, Registerview, logout_view
from profiles.views import ProfileDetailView, UpdateProfileview, ProfilesListView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('profiles', ProfilesListView.as_view(), name='profile_list'),
    path('profile/<pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update/<pk>/', UpdateProfileview.as_view(), name='profile_update'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout", logout_view, name="logout"),
    path('register/', Registerview.as_view(), name='register'),
    path('publicacion/', PostCreateView.as_view(), name='post'),
    path('publicacion/<pk>/', PostDetailView.as_view(), name='post_detail'),
    path("publicacion/like/<pk>/", like_post, name="post_like"),
    path("publicacion/like-ajax/<pk>/", like_post_ajax, name="post_like_ajax"),
    


    path('admin/', admin.site.urls),

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
