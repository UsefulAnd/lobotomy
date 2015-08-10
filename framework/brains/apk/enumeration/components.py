from datetime import datetime
from blessings import Terminal
t = Terminal()


class Components(object):
    def __init__(self, apk):

        super(Components, self).__init__()
        self.apk = apk

    def enum_component(self):

        """
        Enumerate the declared components
        within the target APK
        """

        # Create empty lists for each
        # set of components
        #
        activities = list()
        receivers = list()
        providers = list()
        services = list()

        for a in self.apk.get_activities():
            activities.append(a)

        for r in self.apk.get_receivers():
            receivers.append(r)

        for p in self.apk.get_providers():
            providers.append(p)

        for s in self.apk.get_services():
            services.append(s)

        # Return the main activity
        #
        if self.apk.get_main_activity():
            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Main Activity : ") +
                          self.apk.get_main_activity()))

        if len(activities) != 0:
            for activity in activities:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Activity : ") +
                              activity))

        if len(receivers) != 0:
            for receiver in receivers:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Receiver : ") +
                              receiver))

        if len(providers) != 0:
            for provider in providers:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Provider : ") +
                              provider))

        if len(services) != 0:
            for service in services:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Service : ") +
                              service))