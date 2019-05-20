"""CookBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls, ),
    path("", views.home, name="home"),
    path("tags", views.tags_list, name="tags"),
    path("recipes/<int:pk>", views.RecipeDisplay.as_view(), name="recipe_detail"),
    path("recipes/add", views.RecipeCreate.as_view(), name="recipe-add"),
    path("recipes/<int:pk>/update", views.RecipeUpdate.as_view(), name="recipe-update"),
    path("recipes/<int:pk>/delete", views.RecipeDelete.as_view(), name="recipe-delete"),
    path("tags/add", views.TagCreate.as_view(), name="tag-add"),
    path("tags/<int:pk>/delete", views.TagDelete.as_view(), name="tag-delete"),
    path("tags/<int:pk>", views.tag, name="tag")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
