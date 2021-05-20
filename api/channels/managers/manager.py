import logging

from django.db import models
from django.db.models import Count, F, Sum
from django.db.models.fields.json import KeyTextTransform
from django.db.models.functions import Cast, Coalesce

logger = logging.getLogger(__name__)


class ChannelQueryset(models.QuerySet):
    """Channel Queryset."""

    def calculate_score(self):
        """Calculate score.
        Return:
            Queryset: Queryset
        """
        return self.annotate(
            score_content=Coalesce(
                Sum(
                    Cast(
                        KeyTextTransform("score", "content__src"),
                        models.FloatField()
                    )
                ), 0
            ),
            total_content=Count('content'),
            score_channels=Coalesce(
                Sum(
                    Cast(
                        KeyTextTransform(
                            "score", "tree_channels__content__src"
                        ),
                        models.FloatField()
                    )
                ), 0
            ),
            total_channels=Count('tree_channels__content'),
        ).annotate(
            sum_content=models.ExpressionWrapper(
                F('score_content') + F('score_channels'),  # NOQA
                output_field=models.FloatField()
            ),
            sum_tota=models.ExpressionWrapper(
                F('total_content') + F('total_channels'),
                output_field=models.FloatField()
            ),
        ).annotate(
            average=models.ExpressionWrapper(
                F('sum_content') / F('sum_tota'),  # NOQA
                output_field=models.FloatField()
            )
        )


class ChannelManager(models.Manager):
    """Channel Manager."""

    def get_queryset(self):
        """Get Queryset.
        Return:
            Queryset: Queryset
        """
        return ChannelQueryset(
            self.model, using=self._db
        )
