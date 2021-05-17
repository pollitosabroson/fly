from django.db import models
from django.utils.translation import ugettext_lazy as _


class TitleModel(models.Model):
    """
    Abstract model that defines the auto populated 'name' and
    'order' fields.
    This model must be used as the base for all the models in the project.
    """
    title = models.CharField(
        max_length=500,
        blank=False, null=False,
        verbose_name=_('name')
    )

    class Meta:
        """
        Defination abstract Model
        """
        abstract = True
