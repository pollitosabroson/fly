import logging

from channels.models import Channel
from channels.serializers import BaseChannelSerializers, ChannelSerializer
from contents.serializers import ContentSerializers
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

logger = logging.getLogger(__name__)


class ChannelView(ModelViewSet):
    """List and create hotels."""

    serializer_class = ChannelSerializer
    lookup_field = 'public_id'

    queryset = Channel.objects.all()


class SubChannelView(ModelViewSet):
    """List subchannel."""

    serializer_class = BaseChannelSerializers
    lookup_field = 'public_id'

    queryset = Channel.objects.all()

    def get_queryset(self):
        """we override this method to obtain the data according to the required query
        """
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )
        filter_kwargs = {
            'tree_channels__public_id': self.kwargs[self.lookup_field]
        }
        queryset = self.queryset
        queryset = queryset.filter(**filter_kwargs)
        return queryset


class ChannelContentView(ModelViewSet):
    """List subchannel."""

    serializer_class = ContentSerializers
    lookup_field = 'public_id'
    queryset = Channel.objects.all()

    def get_queryset(self):
        """we override this method to obtain the data according to the required query
        """
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        queryset = get_object_or_404(queryset, **filter_kwargs)
        queryset = queryset.content.all()
        return queryset
