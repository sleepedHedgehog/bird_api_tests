class ApiClient:

    def __init__(self):
        self.host = ""

    def send(self):
        pass

    def post(self, **kwargs):
        pass


class BirdApi(ApiClient):

    def create_bird(self, bird_name=None, bird_type=None, bird_color=None, flight_distance=None):
        return self.post(operation="createBird", bird_name=bird_name,
                         bird_type=bird_type,
                         bird_color=bird_color,
                         flight_distance=flight_distance)
