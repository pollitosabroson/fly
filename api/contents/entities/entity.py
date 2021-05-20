from core.schemas import BaseSchema
from schema import And, Schema


class ContenSourceEntity(BaseSchema):
    """Class for source Entity."""

    schema = Schema(
        {
            'directors': list,
            'author': list,
            'genres': list,
            'writers': list,
            'stars': list,
            'score': And(float, lambda n: 0 < n < 5)
        }
    )

    data = {}

    def __init__(
        self, score, directors=None, author=None,
        genres=None, writers=None, stars=None
    ):
        self.data = {
            "score": score,
            "directors": directors or [],
            "author": author or [],
            "genres": genres or [],
            "writers": writers or [],
            "stars": stars or [],
        }

    def to_dict(self):
        """Convert values to dict.
        Return:
            dict: return all values in dict
        """
        return self.data
