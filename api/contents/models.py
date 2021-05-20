from channels.models import Channel
from core.models import PublicIdModel, TimeStampedModel, TitleModel
from core.models.image_models import content_file_name
from django.db import models
from envs.models import Attributes


class Content(
    TimeStampedModel, PublicIdModel, TitleModel
):

    channel = models.ForeignKey(
        Channel,
        models.DO_NOTHING,
        related_name='content',
        blank=False, null=False
    )

    kind = models.ForeignKey(
        Attributes,
        models.DO_NOTHING,
        related_name='kinds',
        limit_choices_to={'envs_type_name': 'content'}
    )

    content = models.FileField(
        upload_to=content_file_name,
    )

    src = models.JSONField()
