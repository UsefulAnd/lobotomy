from androguard.core.analysis import analysis
from datetime import datetime
from blessings import Terminal
t = Terminal()


class InternalStorageEnum(object):

    values = ["getExternalFilesDir", "getSharedPreferences"]


class InsecureStorage(object):

    name = "storage"

    def __init__(self, apks):

        super(InsecureStorage, self).__init__()
        self.apks = apks
        self.enum = InternalStorageEnum()

    def run(self):

        """
        Search for storage API usage within target class and methods
        """

        x = analysis.uVMAnalysis(self.apks.get_vm())
        vm = self.apks.get_vm()

        if x:
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Performing surgery ...")))
            # Get enum values
            #
            for v in self.enum.values:
                # This returns PathP
                # objects into a list
                #
                paths = x.get_tainted_packages().search_methods("android.content.Context", "{0}".format(v), ".")

                if paths:
                    for p in paths:
                        for method in self.apks.get_methods():
                            if method.get_name() == p.get_src(vm.get_class_manager())[1]:
                                if method.get_class_name() == p.get_src(vm.get_class_manager())[0]:
                                    print(t.green("[{0}] ".format(datetime.now()) +
                                          t.yellow("Found: ") +
                                          "{0}".format(v)))
                                    print(t.green("[{0}] ".format(datetime.now()) +
                                                  t.yellow("Class: ") +
                                                  "{0}".format(method.get_class_name())))
                                    print(t.green("[{0}] ".format(datetime.now()) +
                                                  t.yellow("Method: ") +
                                                  "{0}".format(method.get_name())))
                                    print(method.show())
