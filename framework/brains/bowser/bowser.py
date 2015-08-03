import os
from datetime import datetime
from framework.enums.enums import ADBEnum
from framework.logging.logger import Logger
from subprocess import Popen
from androguard.core.analysis import analysis
from blessings import Terminal
t = Terminal()


class Bowser(object):

    def __init__(self, apks, apk):

        super(Bowser, self).__init__()
        self.apks = apks
        self.apk = apk

    """
    https://github.com/androguard/androguard/blob/master/demos/androguard_ANALYSIS.py

    def display_SEARCH_METHODS(a, x, classes, package_name, method_name, descriptor):
    print "Search method", package_name, method_name, descriptor
    analysis.show_Paths( a, x.get_tainted_packages().search_methods( package_name, method_name, descriptor) )
    """

    def run_bowser(self):

        """
        Run the bowser toolkit
        """

        # Search for parseUri()
        #
        x = analysis.uVMAnalysis(self.apks.get_vm())

        if x:
            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Searching for parseUri()")))
            analysis.show_Paths(self.apks, x.get_tainted_packages().search_methods(".", "parseUri", "."))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Searching for loadUrl()")))
            analysis.show_Paths(self.apks, x.get_tainted_packages().search_methods(".", "loadUrl", "."))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Searching for addJavascriptInterface()")))
            analysis.show_Paths(self.apks, x.get_tainted_packages().search_methods(".", "addJavascriptInterface", "."))

    def run_parse_uri(self):

        """
        Use adb to load up the
        Main Activity and point it back out our blocking
        web server in order to trigger the parsing of the
        intent:// URL scheme
        """

        # Target package and activity
        #
        target = "{0}/{1}".format(self.apk.get_package(), self.apk.get_main_activity())

        print(t.green("[{0}] ".format(datetime.now())) +
              t.yellow("Target URI : ") +
              "{0}".format(target))
        try:
            with open("{0}/framework/config".format(os.getcwd()), "r") as config:
                ip = config.readline()
                config.close()

            url = "http://{0}:5000/services/intent".format(ip)

            Popen(["{0} -n {1} -d {2}".format(ADBEnum.commands.get("am start"), target, url)], shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Command successful : Check you device!"))

        except IOError as e:
            print(t.red("[{0}]".format(datetime.now()) + "Unable to read config"))
            Logger.do_logger(e.message)