from datetime import datetime
from framework.logging.logger import Logger
from blessings import Terminal
t = Terminal()


class Profiler(object):

    def __init__(self, apk):

        super(Profiler, self).__init__()
        self.apk = apk

    def run_profiler(self):

        """
        Profiles the target APK
        """

        print(t.green("[{0}] ".format(datetime.now())) +
              t.yellow("Running profiler against: ") +
              self.apk.filename)

        # Going to wrap this in a try block
        # just in case anything fails
        #
        try:
            package, sdk, backups, files = self.apk.get_package(), \
                self.apk.get_target_sdk_version(), \
                self.apk.get_element("application", "allowBackup"), \
                self.apk.get_files()

            if package:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Package name : ") +
                              package))
            if sdk:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Target SDK version : ") +
                              sdk))
            if backups:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Backups allowed : ") +
                              backups))

            if files:
                for f in files:
                    print(t.green("[{0}] ".format(datetime.now()) +
                                  t.yellow("File : ") +
                                  f))

        except Exception as e:
            # Staying generic for
            # the moment
            #
            print(t.green("[{0}] ".format(datetime.now()) +
                          t.red(e.message)))
            Logger.run_logger(e.message)
