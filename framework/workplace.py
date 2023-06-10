from framework.api_client import BirdApi
from framework.database_steps import DBConnection


class Workplace:
    # self.connect = Connection(api_url)
    # self.db = Database()
    def __init__(self):
        self.db = DBConnection()
        self.bird_api = BirdApi()
