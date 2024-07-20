"""
Main URL handler
URL configuration for DotaPro project.

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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from api.steam_open_id.views import steam_login, get_user_data, logout_view, authenticate
from api.gemini_ai.views import generate_response

urlpatterns = [
    # This would be localhost:8000/admin/
    path('admin/', admin.site.urls),

    # social-auth
    path('', include('social_django.urls', namespace='social')),
    path('steam_login/', steam_login, name='steam_login'),
    path('get_user_data/', get_user_data, name='get_user_data'),
    path('logout/', logout_view, name='logout'),
    path('authenticate/', authenticate, name='authenticate'),
    path('generate_response/', generate_response, name='generate_response'),

    # PSA URLs
    # url(r'', include('social_django.urls', namespace='social'))
    # <a href="{% url 'social:begin' 'provider-name' %}">Login</a>
    # {% url 'social:begin' 'github' %}
    # http://example.com/login/github

    # Add API or other URL patterns as needed using 'include'
    path('api/', include('api.test_routes.urls')),


    # Catch All non-existing routes and redirect to index.html page
    re_path(r'^', TemplateView.as_view(template_name='index.html')),
]
