from framework.brains.surgical.storage import InsecureStorage
from framework.brains.surgical.crypto import Crypto


class SurgicalAPI(object):

    def __init__(self, apk):

        super(self, SurgicalAPI).__init__()
        self.apk = apk
        self.storage = InsecureStorage()
        self.crypto = Crypto()
        self.functions = [f for f in self.storage, self.crypto]

    def run_surgical(self):

        print("testing")

