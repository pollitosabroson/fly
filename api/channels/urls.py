from django.urls import path, re_path

from . import views

urlpatterns = [
    path(
        '',
        views.ChannelView.as_view(
            {
                'get': 'list'
            }
        ),
        name='create_list_channel'
    ),
    re_path(
        r'^(?P<public_id>[\w\-]+)/subchannels$',
        views.SubChannelView.as_view(
            {
                'get': 'list'
            }
        ),
        name='list_envs'
    ),
    re_path(
        r'^(?P<public_id>[\w\-]+)/contents$',
        views.ChannelContentView.as_view(
            {
                'get': 'list'
            }
        ),
        name='list_envs'
    ),
]
