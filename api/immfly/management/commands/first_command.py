from django.core import management
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):
    """
    Command ofr initial proyect.
    """
    help = _(
        'Command to create the ElasticSearch index, create the envs and import'
        ' the country. Example: python manage.py first_command'
    )

    def handle(self, *args, **options):
        """Handle command."""
        # Create envs
        management.call_command(
            'import_envs'
        )

        # Create Channels
        management.call_command(
            'import_channels'
        )
