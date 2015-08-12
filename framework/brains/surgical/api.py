from framework.brains.surgical.storage import InsecureStorage
from framework.brains.surgical.crypto import Crypto
from framework.brains.surgical.logging import Logging
from datetime import datetime
from blessings import Terminal
t = Terminal()


class SurgicalAPI(object):

    def __init__(self, apks):

        super(SurgicalAPI, self).__init__()
        self.apk = apks
        self.storage = InsecureStorage(apks)
        self.crypto = Crypto(apks)
        self.logging = Logging(apks)
        self.functions = [f for f in self.storage, self.crypto, self.logging]

    def run_surgical(self):

        """
        Helper function for API
        """
        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Available functions: ")))

        for f in self.functions:
            print(t.green("[{0}] ".format(datetime.now())) +
                  f.__getattribute__("name"))

        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Enter \'quit\' to exit")))
        while True:
            # Assign target API
            # function
            #
            function = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter function: ")))

            if function == "quit":
                break

            # Match on Class attribute
            # and call run() function
            # of target class
            #
            for f in self.functions:
                if function == f.__getattribute__("name"):
                    f.run()
