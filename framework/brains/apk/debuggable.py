from framework.logging.logger import Logger
from subprocess import Popen
from datetime import datetime
from xml.dom import DOMException
from xml.dom import minidom
from blessings import Terminal
t = Terminal()


class Debuggable(object):
    def __init__(self, directory, apk):

        super(Debuggable, self).__init__()

        self.directory = directory
        self.apk = apk

    def run_debuggable(self):

        """
        This will take a target APK decompile with
        with the apktool.jar and add the attribute
        android:debuggable to the <application/> tag

        It will the rebuild the APK from the output directory
        and sign it with a JKS key so it can be deployed back
        to the target device
        """

        print(t.green("[{0}] ".format(datetime.now())) +
              t.yellow("Decompiling : ") +
              self.apk)

        try:
            Popen(["java -jar apktool.jar d {0} -f -o output/{1}".format(self.apk, self.directory)],
                  shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Adding android:debuggable=\"true\""))

            with open("output/{0}/AndroidManifest.xml".format(self.directory), "r+") as manifest:

                # Using parseString() will prevent
                # XML file size issues
                #
                xml = minidom.parseString(manifest.read())

                # application if of
                # type NodeList
                #
                application = xml.getElementsByTagName("application")
                application[0].setAttribute("android:debuggable", "true")

                # We need to adjust the
                # position of where we begin
                # write and use truncation in order
                # not to corrupt the XML structure
                #
                manifest.seek(0)
                xml.writexml(manifest)
                manifest.truncate()
                manifest.close()

        except OSError as e:
            print(t.red("[{0}]".format(datetime.now()) + "Process exception, check the logs"))
            Logger.run_logger(e.message)

        except IOError as e:
            print(t.red("[{0}]".format(datetime.now()) + "IO exception, check the logs"))
            Logger.run_logger(e.message)

        except DOMException as e:
            print(t.red("[{0}]".format(datetime.now()) + "XML exception, check the logs"))
            Logger.run_logger(e.message)

        try:
            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Building APK : ") +
                  self.directory)

            Popen(["java -jar apktool.jar b output/{0} -o output/{0}/{0}.apk".format(self.directory)],
                  shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Building completed"))

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("APK signing process initiated"))

            Popen(["keytool -genkey -v -keystore lobotomy-key.keystore "
                   "-alias lobotomy -keyalg RSA -keysize 2048 -validity 10000"],
                  shell=True).wait()

            Popen(["jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 "
                   "-keystore lobotomy-key.keystore output/{0}/{0}.apk lobotomy".format(self.directory)],
                  shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Freshly signed APK is located at : ") +
                  "output/{0}/{0}.apk".format(self.directory))

            # We want to create a fresh keystore
            # every time we build and sign a new APK
            #
            Popen(["rm lobotomy-key.keystore"],
                  shell=True).wait()

        except OSError as e:
            print(t.red("[{0}]".format(datetime.now()) + "Process exception, check the logs"))
            Logger.run_logger(e.message)
