from framework.enums.enums import APIMappings
from androguard.core.analysis import analysis
from datetime import datetime
from blessings import Terminal
t = Terminal()


class APIPermissionMappings(object):

    def __init__(self, apk, apks):

        super(APIPermissionMappings, self).__init__()
        self.apk = apk
        self.apks = apks

    @staticmethod
    def run_search_method(apks, x, clz, method):

        analysis.show_Paths(apks, x.get_tainted_packages().search_methods(clz, method, "."))

    def run_find_mapping(self):

        """
        Map permissions to API calls with the analyzed
        bytecode
        """

        # APIMappings enum
        # structure
        #
        enums = APIMappings()

        # VM analysis
        # object
        #
        x = analysis.uVMAnalysis(self.apks.get_vm())

        for permission in self.apk.get_permissions():
            for a, b in enums.mappings.items():
                for c, d in b.items():
                    if "permission" in c:
                        if permission == d:
                            print(t.green("[{0}] ".format(datetime.now()) +
                                          t.yellow("Found permission mapping : ") +
                                          permission))

                            if b.get("class"):
                                for e, f in b.get("class").items():
                                    print(t.green("[{0}] ".format(datetime.now()) +
                                          t.yellow("Searching for : ") +
                                          e))

                                    if f.get("method"):
                                        self.run_search_method(self.apks, x, e, f.get("method"))

                                    elif f.get("methods"):
                                        for method in f.get("methods"):
                                            self.run_search_method(self.apks, x, e, method)

                            elif b.get("classes"):
                                for g, h in b.get("classes").items():
                                    print(t.green("[{0}] ".format(datetime.now()) +
                                          t.yellow("Searching for : ") +
                                          g))

                                    if h.get("method"):
                                        self.run_search_method(self.apks, x, g, h.get("method"))

                                    elif h.get("methods"):
                                        for method in h.get("methods"):
                                            self.run_search_method(self.apks, x, g, method)
