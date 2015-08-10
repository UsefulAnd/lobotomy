from datetime import datetime
from framework.logging.logger import Logger
from framework.enums.enums import D2JEnum
from subprocess import Popen, CalledProcessError
from blessings import Terminal
t = Terminal()


class D2J(object):

    def __init__(self, directory, apk):

        super(D2J, self).__init__()
        self.directory = directory
        self.apk = apk

    def run_d2j(self):

        """
        Run d2j-dex2jar.sh on a target APK and drop JAR into the output
        directory
        """

        print(t.green("[{0}] ".format(datetime.now())) +
              t.yellow("Running dex2jar : ") +
              self.apk)

        try:
            Popen(["{0} output/d2j/{1}.jar {2}".format(D2JEnum.commands.get("decompile"),
                                                       self.directory, self.apk)],
                  shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Finished!"))

        except CalledProcessError as e:
            print(t.red("[{0}] ".format(datetime.now)) + e.returncode)
            Logger.run_logger(e.message)
