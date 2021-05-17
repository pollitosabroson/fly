# -*- coding: utf-8 -*-
import os

from django.db import models


def content_file_name(instance, filename):

    filename = os.path.basename(filename)
    path = (
        f'{instance._meta.verbose_name}/{instance.id}/{filename}'  # NOQA
    )
    data = os.path.join(path)
    return data


class ImageModel(models.Model):
    """Abstract model that defines base channels models
    """

    image = models.ImageField(
        upload_to=content_file_name,
        blank=True, null=True
    )

    class Meta:
        """Defination abstract Model."""

        abstract = True
