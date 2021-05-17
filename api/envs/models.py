import logging

from core.models import TimeStampedModel
from django.db import models

logger = logging.getLogger(__name__)


class Attributes(TimeStampedModel):
    """Envs Model."""

    name = models.CharField(max_length=255)

    envs_type = models.ForeignKey(
        'TypeEnvs',
        models.DO_NOTHING,
        blank=False, null=False,
        related_name="type_envs"
    )

    class Meta:
        verbose_name = "env"
        verbose_name_plural = "envs"

    def __str__(self):
        return self.name

    def to_json(self):
        """conver Hotel value to json for redis.
        Return:
            Dict: Dict with representation value for redis.
        """
        return {
            "id": self.id,
            "created_date": str(self.created_date),
            "last_modified": str(self.last_modified),
            "name": self.name,
            "envs_type": {

            }
        }


class TypeEnvs(TimeStampedModel):
    """Envs Model."""

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "env"
        verbose_name_plural = "envs"

    def __str__(self):
        return self.name

    def to_json(self):
        """conver Hotel value to json for redis.
        Return:
            Dict: Dict with representation value for redis.
        """
        return {
            "id": self.id,
            "created_date": str(self.created_date),
            "last_modified": str(self.last_modified),
            "name": self.name,
        }
