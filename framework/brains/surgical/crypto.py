from androguard.core.analysis import analysis


class Crypto(object):

    name = "crypto"

    def __init__(self, apks):

        super(Crypto, self).__init__()
        self.apks = apks

    def run(self):

        print("crypto")

        return
