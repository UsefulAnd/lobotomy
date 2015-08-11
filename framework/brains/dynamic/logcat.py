import os
import requests
from subprocess import Popen, PIPE, CalledProcessError
from threading import Timer
from framework.logging.logger import Logger
from datetime import datetime
from blessings import Terminal

t = Terminal()


class Logcat(object):
    def __int__(self):

        super(Logcat, self).__init__()

    @staticmethod
    def http_handler(output):

        """
        Handler for submitting logs to the
        logcat web service
        """

        try:
            with open("{0}/framework/config".format(os.getcwd()), "r") as config:
                ip = config.readline()
                config.close()

            # Populate POST request
            # with output from
            # Logcat
            #
            data = {"data": output}

            # TODO - 07/26/2015
            # Remove hardcoded string and add to enums
            #
            r = requests.post("http://{0}:5000/services/logcat/update".format(ip.strip("\n")), data=data)

            if r.text == "Success":
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Success!")))
            else:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.red("Error! ") +
                              "Check flask.log"))

        except IOError as e:
            print(t.red("[{0}] ".format(datetime.now()) +
                        e))
            Logger.run_logger(e)

        except requests.ConnectionError as e:
            print(t.red("[{0}] ".format(datetime.now()) +
                        e.response))
            Logger.run_logger(e.response)

        return

    def timeout(self, process):

        """
        Callback to handle process
        timeouts
        """

        if process.poll() is None:
            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Gathering logs ...")))

        # Call
        # http_handler() with output
        #
        out = process.communicate()
        self.http_handler(out)

    def run_logcat(self):

        """
        Run Logcat with a keyword search that dumps
        output
        """

        while True:
            result = raw_input(t.green("[{0}] ".format(datetime.now()) +
                                       t.yellow("Would you like to run Logcat? { Y || N } : ")))
            if result == "N":
                break

            elif result == "Y":
                keyword = raw_input(t.green("[{0}] ".format(datetime.now()) +
                                            t.yellow("Enter keyword search : ")))
                try:
                    p = Popen("adb logcat -d | grep {0}".format(keyword),
                              stdout=PIPE,
                              stderr=PIPE,
                              shell=True)

                    # Create a new Timer()
                    # object and handle process timeouts
                    # with a callback
                    #
                    thread = Timer(3.0, self.timeout, [p])
                    thread.start()
                    thread.join()

                except CalledProcessError as e:
                    print(t.red("[{0}] ".format(datetime.now()) +
                                e.returncode))
                    Logger.run_logger(e.message)

                except IOError as e:
                    print(t.red("[{0}] ".format(datetime.now()) +
                                e.message))
                    Logger.run_logger(e.message)
