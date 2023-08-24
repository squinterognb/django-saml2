"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
import django_saml2_auth.views

urlpatterns = [
    path('', include(('public.urls', 'public'), namespace='public')),
    re_path(r'^sso/', include('django_saml2_auth.urls')),
    #re_path(r'^accounts/login/$', django_saml2_auth.views.signin),
    path('admin/login/', django_saml2_auth.views.signin),
    #re_path(r'^accounts/logout/$', django_saml2_auth.views.signout),
    #re_path(r'^admin/logout/$', django_saml2_auth.views.signout),
    path('private/', include(('private.urls', 'private'), namespace="private")),
    path('admin/', admin.site.urls),
]
