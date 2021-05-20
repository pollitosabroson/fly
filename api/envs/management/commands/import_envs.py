import logging

from django.core.management.base import BaseCommand
from envs.models import Attributes, TypeEnvs
from tqdm import tqdm

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Command to update all references."""

    help = (
        "Command to update all references."
        "example to execution: python manage.py import_envs"
    )

    def handle(self, *args, **options):

        type_envs = {
            TypeEnvs.LANGUAGE: ['ES', 'EU', 'PT', 'IT'],
            TypeEnvs.CONTENT: [
                'gif', 'jpg', 'tif', 'png', 'bmp', 'svg',
                'doc', 'pdf', 'txt', 'rtf', 'html', 'epub',
                'avi', 'mpeg', 'mov', 'mkv', 'asf', 'QT', 'webM', 'flv', 'RM',
                'DVD', 'xls', 'csv', 'ppt',
            ]
        }

        for key, value in tqdm(type_envs.items(), total=len(type_envs)):
            type_env, _ = TypeEnvs.objects.get_or_create(
                name=key
            )
            for attribute in value:
                Attributes.objects.get_or_create(
                    name=attribute,
                    envs_type=type_env
                )
