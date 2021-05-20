import logging

from envs.models import TypeEnvs
from rest_framework import serializers

logger = logging.getLogger(__name__)


class EnvsSerializer(serializers.ModelSerializer):
    """List hotel Serializer"""

    class Meta:
        model = TypeEnvs
        fields = ('name', 'id')

    def to_representation(self, instance):

        return instance.to_json()
