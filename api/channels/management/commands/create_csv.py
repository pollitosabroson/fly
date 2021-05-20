import logging
from datetime import datetime

from channels.repositories import ChannelRepository
from core.csv import ParseCsv
from django.core.management.base import BaseCommand
from tqdm import tqdm

logger = logging.getLogger(__name__)


def csv_name(str_name):
    """Add extension for file.
    return:
        String: File name with the extension .csv
    """
    return f'{str_name}.csv'


class Command(BaseCommand):
    """Command to update all references."""

    help = (
        "Command to update all references."
        "example to execution: python manage.py create_csv"
    )

    HEADERS = ['id', 'public_id', 'chanel_name', 'average', ]

    def add_arguments(self, parser):
        """Add Arguments."""
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "-cn",
            "--csv_name",
            required=False,
            help=("csv name"),
            type=csv_name,
            default=f'average_channels_{datetime.now().strftime("%d_%b_%Y")}'
        )

    def handle(self, *args, **options):
        list_channels = []
        channels = ChannelRepository.query_all_average().order_by('-average')
        list_channels.append(
            self.HEADERS
        )
        for channel in tqdm(channels):
            list_channels.append(
                [
                    channel.id, channel.public_id,
                    channel.title, channel.score
                ]
            )
        file_name = options.get('csv_name')
        ParseCsv.create_csv(
            file_name=file_name,
            row_list=list_channels
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'The file {file_name} was created with a total of {channels.count()} channels'  # NOQA
            )
        )
