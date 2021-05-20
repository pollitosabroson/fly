import logging

from channels.models import Channel
from contents.serializers import ContentSerializers
from rest_framework import serializers

logger = logging.getLogger(__name__)


class BaseChannelSerializers(serializers.ModelSerializer):

    id = serializers.CharField(
        source='public_id'
    )
    contents = serializers.SerializerMethodField()
    language = serializers.CharField(
        source='language.name'
    )

    class Meta:
        model = Channel
        fields = ['title', 'id', 'score', 'image', 'contents', 'language', ]

    def get_contents(self, obj):
        """Convert id for public_id.
        Args:
            obj(instance): Channel instance
        Return:
            str: Channel public_id
        """
        return ContentSerializers(
            obj.content.all(),
            many=True
        ).data


class ChannelSerializer(BaseChannelSerializers):
    """List Channel Serializer"""

    sub_channels = serializers.SerializerMethodField()

    class Meta:
        model = Channel
        fields = BaseChannelSerializers.Meta.fields + ['sub_channels', ]

    def get_sub_channels(self, obj):
        """Get all subchannels.
        Args:
            obj(instance): Channel instance
        Return:
            list: List all subchannels
        """
        return BaseChannelSerializers(
            obj.tree_channels.all(), many=True
        ).data
