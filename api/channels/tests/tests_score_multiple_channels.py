import logging

import pytest
from channels.repositories import ChannelRepository

from .factory import ChannelFactory, Contentfactory

logger = logging.getLogger(__name__)


@pytest.mark.django_db
@pytest.mark.urls('immfly.urls')
class TestSingleChannelScore:
    """Specific tests for list hotel."""

    def test_calculte_single_channel(self, client):
        """Test to validate that a user will be edited with the parameters."""
        total_content = 5
        score = round(
            total_content * Contentfactory.DEFAULT_SCORE / total_content,
            2
        )
        test_channel = ChannelFactory.create_channel_wiht_content(
            total_contents=total_content
        )
        channels = ChannelRepository.query_all_average().order_by('-average')
        for channel in channels:
            if test_channel.public_id == channel.public_id:
                assert score == channel.score
