from androguard.core.analysis import analysis
from datetime import datetime
from blessings import Terminal
t = Terminal()


class IPCEnum(object):

    values = {

        "android.app.Activity":

            [

                "onCreate",
                "onNewIntent",
                "getIntent",
                "startActivities",
                "startActivity",
                "startActivityForResult",
                "startActivityFromChild",
                "startActivityFromFragment",
                "startActivityIfNeeded",
                "startIntentSender",
                "startIntentSenderForResult",
                "startIntentSenderFromChild",

            ],

        "android.content.Intent":

            [

                "parseUri",
                "parseIntent"

            ],

        "android.content.BroadcastReceiver":

            [

                "onReceive"

            ],

        "android.content.Context":

            [

                "startIntentSender",
                "startService",
                "stopService",
                "startActivities",
                "sendStickyOrderedBroadcast",
                "sendStickyOrderedBroadcastAsUser",
                "sendStickyBroadcast",
                "sendStickyOrderedBroadcast",
                "sendStickyOrderedBroadcastAsUser",
                "sendBroadCast",
                "bindService"

            ],

        "android.app.Service":

            [

                "onBind",
                "onRebind",
                "onStart",
                "onStartCommand",
                "onCreate"

            ]

    }


class IPC(object):

    name = "ipc"

    def __init__(self, apks):

        super(IPC, self).__init__()
        self.apks = apks
        self.enum = IPCEnum()

    def run(self):

        x = analysis.uVMAnalysis(self.apks.get_vm())
        vm = self.apks.get_vm()

        selections = ["activity", "intent", "receiver", "context", "service"]

        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Available selections: ")))

        for s in selections:
            print(t.green("[{0}] ".format(datetime.now())) + "{0}".format(s))

        selection = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter selection: ")))

        for a, b in self.enum.values.items():
            if selection in a.lower():
                for c in b:
                    paths = x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                    if paths:
                        for p in paths:
                            for method in self.apks.get_methods():
                                if method.get_name() == p.get_src(vm.get_class_manager())[1]:
                                    if method.get_class_name() == p.get_src(vm.get_class_manager())[0]:
                                        print(t.green("[{0}] ".format(datetime.now()) +
                                              t.yellow("Found: ") +
                                              "{0}".format(c)))
                                        print(t.green("[{0}] ".format(datetime.now()) +
                                                      t.yellow("Class: ") +
                                                      "{0}".format(method.get_class_name())))
                                        print(t.green("[{0}] ".format(datetime.now()) +
                                                      t.yellow("Method: ") +
                                                      "{0}".format(method.get_name())))
                                        print(method.show())