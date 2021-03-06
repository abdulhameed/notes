"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from notes import settings
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Users
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('edit-profile/', views.edit_profile, name="edit-profile"),

    # Share
    path('share/', include('share.urls', namespace='share')),

    # API
    path('api/', include('api.urls', namespace='api')),

    # Notes
    path('new-note/', views.new_note, name='new-note'),
    path('view-note/<int:note_id>/', views.view_note, name='view-note'),
    path('download-note/<int:note_id>/<filetype>/', views.download_note, name='download-note'),
    path('edit-note/<int:note_id>/', views.edit_note, name='edit-note'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete-note'),

    # Notebooks
    path('new-notebook/', views.new_notebook, name='new-notebook'),
    path('view-notebook/<int:notebook_id>/', views.view_notebook, name='view-notebook'),
    path('download-notebook/<int:notebook_id>/<filetype>/', views.download_notebook, name='download-notebook'),
    path('edit-notebook/<int:notebook_id>/', views.edit_notebook, name='edit-notebook'),
    path('delete-notebook/<int:notebook_id>/', views.delete_notebook, name='delete-notebook'),

    # Notebook selection operations
    path(r'delete-notes/<note_ids>/', views.delete_notes, name='delete-notes'),
    path(r'move-notes/<note_ids>/', views.move_notes, name='move-notes'),
    path(r'merge-notes/<note_ids>/', views.merge_notes, name='merge-notes'),

    # Trash bin
    path('trash/', include('trash.urls', namespace='trash')),

    # Search
    path('search-notes/', views.search, name='search-notes'),
    path('search-notebook/<int:notebook_id>/', views.search_notebook, name='search-notebook'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
