from datetime import datetime
from blessings import Terminal
from framework.logging.logger import Logger
from xml.dom import DOMException

t = Terminal()


class AttackSurface(object):
    def __init__(self, apk):

        super(AttackSurface, self).__init__()
        self.apk = apk

    @staticmethod
    def run_parse_xml(xml, component, name):

        """
        Parse the XML object (AndroidManifest.xml)
        returned from Androguard and perform enumeration tasks that helps
        build the attacksurface for the target APK
        """

        # Get all the elements within
        # the xml object
        #
        try:
            # Activities
            #
            if component == "activity":

                # Get all the
                # tag elements
                #
                activities = xml.getElementsByTagName("activity")

                for activity in activities:

                    if activity.getAttribute("android:name") == name:

                        # Enumerate exported Activities
                        #
                        if activity.getAttribute("android:exported"):

                            if activity.getAttribute("android:exported") == "true":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow(" {0} : ".format(name)) +
                                              t.cyan("Found exported activity!")))

                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : exported : ".format(name)) +
                                              "{0}".format(activity.getAttribute("android:exported"))))

                        # Enumerate Activities
                        # with taskAffinity
                        #
                        if activity.getAttribute("android:taskAffinity"):
                            print(t.green("[{0}]".format(datetime.now()) +
                                          t.yellow(" {0} : ".format(name)) +
                                          t.cyan("Found Activity with taskAffinity!")))

                            print(t.green("[{0}] ".format(datetime.now()) +
                                          t.yellow("{0} : taskAffinity : ".format(name)) +
                                          "{0}".format(activity.getAttribute("android:taskAffinity"))))

                        # Enumerate Activities
                        # with launchMode
                        #
                        if activity.getAttribute("android:launchMode"):
                            print(t.green("[{0}]".format(datetime.now()) +
                                          t.yellow(" {0} : ".format(name)) +
                                          t.cyan("Found Activity with launchMode!")))

                            if activity.getAttribute("android:launchMode") == "0":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : launchMode : ".format(name)) +
                                              "multiple"))

                            elif activity.getAttribute("android:launchMode") == "1":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : launchMode : ".format(name)) +
                                              "singleTop"))

                            elif activity.getAttribute("android:launchMode") == "2":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : launchMode : ".format(name)) +
                                              "singleTask"))

                            elif activity.getAttribute("android:launchMode") == "3":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : launchMode : ".format(name)) +
                                              "singleInstance"))

                        intents = activity.getElementsByTagName("intent-filter")
                        schemes = list()

                        # Enumerate data
                        # schemes
                        #
                        if intents:
                            for intent in intents:
                                data = intent.getElementsByTagName("data")
                                if data:
                                    for d in data:
                                        if d.getAttribute("android:scheme"):
                                            schemes.append(d.getAttribute("android:scheme"))

                            # Remove duplicate schemes
                            #
                            results = list(set(schemes))

                            if results:
                                print(t.green("[{0}]".format(datetime.now()) +
                                              t.yellow(" {0} : ".format(name)) +
                                              t.cyan("Found Activity with schemes!")))

                                for r in results:
                                    print(t.green("[{0}] ".format(datetime.now()) +
                                                  t.yellow("{0} : ".format(name)) +
                                                  t.yellow("scheme : ") + "{0}".format(r)))

            # Receivers
            #
            elif component == "receiver":

                # Get all the
                # tag elements
                #
                receivers = xml.getElementsByTagName("receiver")

                for receiver in receivers:
                    if receiver.getAttribute("android:name") == name:
                        if receiver.getAttribute("android:exported"):
                            if receiver.getAttribute("android:exported") == "true":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : ".format(name)) +
                                              t.cyan("Found exported receiver!")))

                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : exported : ".format(name)) +
                                              "{0}".format(receiver.getAttribute("android:exported"))))

            elif component == "provider":

                providers = xml.getElementsByTagName("provider")

                for provider in providers:
                    if provider.getAttribute("android:name") == name:
                        if provider.getAttribute("android:exported"):
                            if provider.getAttribute("android:exported") == "true":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : ".format(name)) +
                                              t.cyan("Found exported provided!")))

                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : exported : ".format(name)) +
                                              "{0}".format(provider.getAttribute("android:exported"))))

            elif component == "service":

                services = xml.getElementsByTagName("service")

                for service in services:
                    if service.getAttribute("android:name") == name:
                        if service.getAttribute("android:exported"):
                            if service.getAttribute("android:exported") == "true":
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("{0} : ".format(name)) +
                                              t.cyan("Found exported service!")))

                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.cyan("{0} : exported : ".format(name)) +
                                              "{0}".format(service.getAttribute("android:exported"))))

                            if service.getAttribute("android:process"):
                                print(t.green("[{0}] ".format(datetime.now()) +
                                              t.cyan("{0} : process : ".format(name)) +
                                              "{0}".format(service.getAttribute("android:process"))))

        except DOMException as e:
            print(t.red("[{0}]".format(datetime.now()) + "XML exception, check the logs"))
            Logger.run_logger(e.message)

    def run_enum_attack_surface(self):

        """
        Enumerate the attacksurface for the target APK
        """

        # Grab lists for components
        #
        activities = self.apk.get_activities()
        receivers = self.apk.get_receivers()
        providers = self.apk.get_providers()
        services = self.apk.get_services()

        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Activites")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))

        # Enumerate activities
        #
        for activity in activities:
            self.run_parse_xml(self.apk.get_AndroidManifest(), "activity", activity)
            filters = self.apk.get_intent_filters("activity", activity)
            for key, values in filters.items():
                if key == "action":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : action : ".format(activity)) +
                                      value))
                if key == "category":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : category : ".format(activity)) +
                                      value))

        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Receivers")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))

        # Enumerate receivers
        #
        for receiver in receivers:
            self.run_parse_xml(self.apk.get_AndroidManifest(), "receiver", receiver)
            filters = self.apk.get_intent_filters("receiver", receiver)
            for key, values in filters.items():
                if key == "action":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : action : ".format(receiver)) +
                                      value))
                if key == "category":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : category : ".format(receiver)) +
                                      value))

        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Providers")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))

        # Enumerate providers
        #
        for provider in providers:
            self.run_parse_xml(self.apk.get_AndroidManifest(), "provider", provider)
            filters = self.apk.get_intent_filters("provider", provider)
            for key, values in filters.items():
                if key == "action":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : action : ".format(provider)) +
                                      value))
                if key == "category":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : category : ".format(provider)) +
                                      value))

        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Services")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("---------")))

        # Enumerate services
        #
        for service in services:
            self.run_parse_xml(self.apk.get_AndroidManifest(), "service", services)
            filters = self.apk.get_intent_filters("service", services)
            for key, values in filters.items():
                if key == "action":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : action : ".format(service)) +
                                      value))
                if key == "category":
                    for value in values:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("{0} : category : ".format(service)) +
                                      value))
