from androguard.core.analysis import analysis
from datetime import datetime
from blessings import Terminal
t = Terminal()


class CryptoEnum(object):

    values = {

        "java.security.Key": [

            "getAlgorithm"

        ],

        "javax.crypto.spec.SecurityKeySpec": [

            "SecurityKeySpec",
            "getAlgorithm"

        ],

        "javax.crypto.Cipher": [

            "Cipher",
            "doFinal",
            "getIV",
            "getInstance"
        ],

        "javax.crypto.KeyGenerator": [

            "generateKey",
            "getAlgorithm",
            "getInstance"

        ]

    }


class Crypto(object):

    name = "crypto"

    def __init__(self, apks):

        super(Crypto, self).__init__()
        self.apks = apks
        self.enum = CryptoEnum()

    def run(self):

        """
        Search for crypto API usage within target class and methods
        """

        x = analysis.uVMAnalysis(self.apks.get_vm())
        vm = self.apks.get_vm()

        if x:
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Performing surgery ...")))
            # Get enum values
            #
            for a, b in self.enum.values.items():
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