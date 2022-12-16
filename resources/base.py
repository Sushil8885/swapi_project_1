not_implemented_error_msg = "This method has not been implemented"

class ResourceBase(object):
    """
    Base class representing required methods to be implemented by all resources
    classes
    """

    resources = ["planets", "spaceships", "people", "vehicles", "films", "species"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError("This method has not been implemented")

    def get_resources_urls(self, resource):
        raise NotImplementedError("This method has not been implemented")



