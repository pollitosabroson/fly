import logging

from envs.models import TypeEnvs
from envs.serializers import EnvsSerializer
from rest_framework.viewsets import ModelViewSet

logger = logging.getLogger(__name__)


class EnvsView(ModelViewSet):
    """List and create hotels."""

    serializer_class = EnvsSerializer
    lookup_field = 'public_id'

    queryset = TypeEnvs.objects.all()
