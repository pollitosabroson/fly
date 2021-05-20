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
        """convery attribute value to json.
        Return:
            Dict: Dict with representation value for json.
        """
        return {
            "id": self.id,
            "created_date": str(self.created_date),
            "last_modified": str(self.last_modified),
            "name": self.name,
            "envs_type": {
                "id": self.envs_type.id,
                "name": self.envs_type.name,
            }
        }

    @classmethod
    def get_attributes_by_typeenvs(cls, env_type):

        values = cls.objects.filter(
            envs_type=env_type
        )
        return values


class TypeEnvs(TimeStampedModel):
    """Envs Model."""

    LANGUAGE = "Language"
    CONTENT = "Type Content"

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "env"
        verbose_name_plural = "envs"

    def __str__(self):
        return self.name

    def to_json(self):
        """conver ENV value to json for JSON.
        Return:
            Dict: Dict with representation value for redis.
        """
        return {
            "id": self.id,
            "created_date": str(self.created_date),
            "last_modified": str(self.last_modified),
            "name": self.name,
            "attributes": [
                {
                    "id": x.id,
                    "name": x.name,
                }
                for x in self.type_envs.all()
            ]
        }

    @classmethod
    def get_env(cls, env_name):
        try:
            return cls.objects.get(name=env_name)
        except cls.DoesNotExist:
            return None
