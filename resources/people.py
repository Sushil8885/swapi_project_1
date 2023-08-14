from base import ResourceBase
from utils.fetch_data import fetch_data


class Characters(ResourceBase):
    """
    Resources class (plural)
    """

    def __init__(self):
        super().__init__()
        self.relative_url = "api/people"

    def get_count(self):
        plural_character_url = self.home_url + self.relative_url

        response = fetch_data(plural_character_url) if plural_character_url else {}
