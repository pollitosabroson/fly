import logging

from channels.managers import ChannelManager
from core.models import ImageModel, PublicIdModel, TimeStampedModel, TitleModel
from django.db import models
from envs.models import Attributes

logger = logging.getLogger(__name__)


class Channel(
    TimeStampedModel, ImageModel, PublicIdModel, TitleModel
):

    language = models.ForeignKey(
        Attributes,
        models.DO_NOTHING,
        related_name='languages',
        limit_choices_to={'envs_type__name': 'languages'}
    )

    tree_channel = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        related_name='tree_channels',
        blank=True, null=True
    )

    objects = ChannelManager()

    @property
    def score(self):
        """Return score from channel.
        Return:
            Float: score
        """
        value = self._calculate_sinlge_score(
            channel_id=self.id
        )
        return round(value.average, 2)

    @classmethod
    def _calculate_sinlge_score(cls, channel_id):
        """Calculate score from one channel.
        Args:
            channel_id(int): Channel id
        Return:
            Queryset: queryset.
        """
        return cls.objects.filter(
            id=channel_id
        ).calculate_score().last()
