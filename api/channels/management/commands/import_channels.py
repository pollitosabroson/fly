import logging
import random
import string

from channels.models import Channel
from contents.entities import ContenSourceEntity
from contents.models import Content
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from envs.models import Attributes, TypeEnvs
from tqdm import tqdm

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Command to update all references."""

    help = (
        "Command to update all references."
        "example to execution: python manage.py import_channels"
    )

    CHANNEL_NAME = [
        'Show Stellar', 'Showorzo', 'Show Scoot', 'Tv Reboot', 'Tvjet',
        'Show Port', 'Tv Truth', 'Tv Variable', 'Show Module', 'Tvpad',
        'Showlia', 'Show Logic', 'Show Spirit', 'Tv Abstract', 'Tv Sign',
        'Tvorzo', 'Show Omni', 'Show Sprite', 'Show Verse', 'Tv Scope',
        'Showzilla', 'Show Cubed', 'Show Level', 'Show Insight'
    ]

    SHOW_NAME = [
        'Zombie Adventures', 'Stray Adventures', 'Voodoo Legend',
        'Enigma Stories', 'Heaven Grave', 'Freak Oracle', 'Anonymous Kind',
        'Angelbones', 'Angelgift', 'Moonring', 'Smoke Adventures', 'Paperkin',
        'Naughty Drama', 'Warrior Fantasy', 'Rainy Legend', 'Monster Promises',
        'Alternate Doom', 'Distant Doodles', 'Winterbot', 'Metalbow'
    ]

    FILE_NAME = [
        'Storm Fantasy', 'Anti-Social Story', 'Yesterdays Fantasies',
        'Thunder Fantasy', 'Deadly Everyday', 'Shady Galaxy', 'Space Morning',
        'Spiderstar', 'Dreamshock',
    ]

    AUTHORS = [
        'Julius Price', 'Jimmy Adkins', 'Wm Graham', 'Andy Kelley',
        'Jacob Andrews', 'Shannon Bailey', 'Beulah Rose',
        'Minnie Long', 'Brittany Blair', 'Ruth Banks', 'Melody Moody',
        'Lamar Gardner',
    ]

    DIRECTORS = [
        'Alexander Bush', 'Eileen Fox', 'Mindy Rios', 'Carrie Owen',
        'Billy Ellis', 'Hazel Owens', 'Ricky Powell', 'Steven Shaw',
        'Vanessa Cummings', 'Marilyn Watts', 'Elisa Sanchez', 'Tonya Morris',
        'Emma Ramos',
    ]

    GENRES = [
        'Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance',
        'Thriller', 'Western',
    ]

    WRITERS = [
        'Faye Lawrence', 'Morris Young', 'Violet Ray', 'Angelina Copeland',
        'Mabel Ross', 'Jeff Greene', 'Harry Armstrong', 'Johnathan Brown',
        'Elisa Wilkins', 'Ed Brady',
    ]

    def handle(self, *args, **options):

        languages = Attributes.objects.filter(
            envs_type__name=TypeEnvs.LANGUAGE
        )
        attributes = Attributes.objects.filter(
            envs_type__name=TypeEnvs.CONTENT
        )
        for channel_name in self.CHANNEL_NAME:
            channel, _ = Channel.objects.get_or_create(
                title=channel_name,
                language=random.choice(languages)
            )
            for _ in tqdm(range(random.randrange(1, 10))):
                src = ContenSourceEntity(
                    score=round(random.uniform(0, 10), 2),
                    directors=self.get_random_values(self.DIRECTORS),
                    author=self.get_random_values(self.AUTHORS),
                    genres=self.get_random_values(self.GENRES),
                    writers=self.get_random_values(
                        self.WRITERS, random_range=3
                    ),
                )
                kind = random.choice(attributes)
                content = Content(
                    channel=channel,
                    kind=kind,
                    src=src.to_dict()
                )
                file_name = f'{slugify(random.choice(self.FILE_NAME))}.{kind.name.lower()}'  # NOQA
                content.save()
                content.content.save(
                    file_name,
                    ContentFile(
                        f"{','.join(x for x in string.ascii_letters)}".encode()  # NOQA
                    )
                )

    @staticmethod
    def get_random_values(values, random_range=5):
        """Create list with random values.
        Args:
            values(List): List with content
            random_range(int): Number to calculate the random
        Return:
            List: List with random values
        """
        return [
            random.choice(values)
            for _ in range(random.randrange(1, random_range))
        ]
