import logging
import random

from channels.models import Channel
from contents.entities import ContenSourceEntity
from contents.models import Content
from django.core.files.base import ContentFile
from envs.models import Attributes, TypeEnvs

logger = logging.getLogger(__name__)


class Contentfactory:
    """Class in charge of creating content objects."""

    DEAFUALT_CONTENT_NAME = 'Test_content_factory'
    DEFAULT_SCORE = 8.5

    @classmethod
    def _get_content(cls, channel, **kwargs):
        """
        Return instance content
        """
        value = kwargs.get('value', 1)
        attributes = Attributes.objects.filter(
            envs_type__name=TypeEnvs.CONTENT
        )
        kind = random.choice(attributes)
        src = cls.get_sourcre()
        content = Content(
            channel=channel,
            kind=kind,
            src=src.to_dict()
        )
        content.save()
        file_name = f'{cls.DEAFUALT_CONTENT_NAME}-{value}.{kind.name.lower()}'  # NOQA
        content.save()
        content.content.save(
            file_name,
            ContentFile(
                "This is the content".encode()
            )
        )
        return content

    @staticmethod
    def get_sourcre(score=DEFAULT_SCORE):
        """Create source content.
        Arg:
            Score(Float): Total score for content
        Return:
            Dict: Dict with all source.
        """
        src = ContenSourceEntity(
            score=score,
            directors=['directors 1', 'directors 3'],
            author=['author 1', 'author 2'],
            genres=['genres 1', 'genres 2'],
            writers=['writers 1', 'writers 2'],
        )
        return src

    @classmethod
    def get_content(cls, channel, **kwargs):
        """Get single content.
        Args:
            name(str): name of content
            channel(Instance): channel
        Return:
            Instance: Instance of content
        """
        content = cls._get_content(
            channel=channel,
            **kwargs
        )
        return content


class ChannelFactory:
    """Class in charge of creating channel objects."""

    DEFAULT_TEST_CHANNEL_NAME = 'channel_test'
    DEFUALT_CONTENT = 5

    def _get_channel(channel_name=DEFAULT_TEST_CHANNEL_NAME, **kwargs):
        """
        Return instance channel
        """
        languages = Attributes.objects.filter(
            envs_type__name=TypeEnvs.LANGUAGE
        )
        language = random.choice(languages)
        channel_name = f'{channel_name}-{language.name}'
        channel, _ = Channel.objects.get_or_create(
            title=channel_name,
            language=language
        )
        channel.save()
        return channel

    @classmethod
    def get_channel(cls, **kwargs):
        """get single channel
        Return:
            Instance: Channel instance
        """
        return cls._get_channel(
            **kwargs
        )

    @classmethod
    def create_channel_wiht_content(cls, **kwargs):
        """Create Channel with multiples contest.
        Return:
            Instance: Channel instance
        """
        if not kwargs.get('channel'):
            channel = cls._get_channel(
                name=kwargs.get('channel_name', cls.DEFAULT_TEST_CHANNEL_NAME)
            )
        for value in range(0, kwargs.get('total_contents', cls.DEFUALT_CONTENT)):  # NOQA
            Contentfactory.get_content(
                channel=channel,
                value=value
            )
        return channel
