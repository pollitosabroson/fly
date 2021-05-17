from core.models import ImageModel, PublicIdModel, TimeStampedModel, TitleModel
from django.db import models
from envs.models import Attributes


class Channel(
    TimeStampedModel, ImageModel, PublicIdModel, TitleModel
):

    language = models.ForeignKey(
        Attributes,
        models.DO_NOTHING,
        related_name='languages',
        limit_choices_to={'envs_type_name': 'languages'}
    )

    tree_channel = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        related_name='tree_channels',
        blank=True, null=True
    )
