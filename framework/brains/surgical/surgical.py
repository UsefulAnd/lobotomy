from .storage import InsecureStorage


class SurgicalAPI(object):

    def __init__(self):

        super(self, SurgicalAPI).__init__()

        self.storage = InsecureStorage()

    def do_surgery(self):

        return