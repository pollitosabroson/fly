import logging

from contents.models import Content
from rest_framework import serializers

logger = logging.getLogger(__name__)


class ContentSerializers(serializers.ModelSerializer):

    id = serializers.CharField(
        source='public_id'
    )
    kind = serializers.CharField(
        source='kind.name'
    )

    class Meta:
        model = Content
        fields = ['id', 'kind', 'content', 'src']
