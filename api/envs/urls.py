from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.EnvsView.as_view(
            {
                'get': 'list'
            }
        ),
        name='create_list_envs'
    ),
]
