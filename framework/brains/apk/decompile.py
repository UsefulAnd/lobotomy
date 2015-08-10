from framework.logging.logger import Logger
from subprocess import Popen, CalledProcessError
from datetime import datetime
from blessings import Terminal
t = Terminal()


class Decompile(object):
    def __init__(self, directory, apk):

        super(Decompile, self).__init__()

        self.apk = apk
        self.directory = directory

    def run_decompile(self):

        """
        Decompile target APK with apktool.jar
        """

        print(t.green("[{0}] ".format(datetime.now())) +
              t.yellow("Decompiling : ") +
              self.apk)

        try:
            Popen("java -jar apktool.jar d {0} -f -o output/{1}".format(self.apk, self.directory),
                  shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Finished!"))

        except CalledProcessError as e:
            print(t.red("[{0}] ".format(datetime.now)) + e.returncode)
            Logger.run_logger(e.message)
