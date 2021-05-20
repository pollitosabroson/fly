from channels.models import Channel


class ChannelRepository:

    MODEL = Channel

    @classmethod
    def query_all_average(cls):
        """return query with average.
        return:
            Queryset: Queryser
        """
        return cls.MODEL.objects.all().calculate_score()
