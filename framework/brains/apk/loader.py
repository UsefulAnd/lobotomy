from datetime import datetime
from androguard.core.bytecodes.apk import APK
from androguard.core.androgen import AndroguardS
from blessings import Terminal
t = Terminal()


class Loader(object):

    def __init__(self, apk):

        super(Loader, self).__init__()
        self.apk = apk

    def run_loader(self):

        """
        Load the target APK and return
        the loaded instance, which will
        be stored as a global
        """

        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Loading : ") +
                      "{0}".format(self.apk)))

        return APK(self.apk), AndroguardS(self.apk)