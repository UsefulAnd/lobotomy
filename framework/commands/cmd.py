from datetime import datetime
from cmd2 import Cmd as Lobotomy
from blessings import Terminal
from framework.logging.logger import Logger
t = Terminal()


class Run(Lobotomy):

    def __init__(self):

        Lobotomy.__init__(self)

    # APK related commands
    # --------------------
    # loader, decompile, debuggable,
    # profiler, permissions, components
    #

    @staticmethod
    def do_loader(args):

        """
        Description: Load target APK for analysis wth androguard --

        Requirements: Target APK

        Usage: loader </path/to/apk>
        """

        try:
            from framework.brains.apk.loader import Loader
            loader = Loader(args)
            global apk, apks
            apk, apks = loader.do_loader()

        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Loader"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_decompile(args):

        """
        Description: Decompile target APK with apktool.jar

        Requirements: Target APK

        Usage: decompile <name_of_output_directory> && </path/to/apk>
        """

        try:
            from framework.brains.apk.decompile import Decompile
            decompile = Decompile(args.split()[0], args.split()[1])
            decompile.do_decompile()

        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Decompile"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_profiler(args):

        """
        Description: Run profiling on the target APK loaded

        Requirements: Loaded APK

        Usage: profiler
        """

        try:
            from framework.brains.apk.enumeration.profiler import Profiler
            p = Profiler(globals()["apk"])
            p.run_profiler()

        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Profiler"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_permissions(args):

        """
        Description: List enumeration and api mappings from target APK

        Requirements: Loaded APK

        Usage: permissions <list> || <map>
        """

        try:
            from framework.brains.apk.enumeration.permissions import Permissions
            p = Permissions(globals()["apk"], globals()["apks"])

            if args == "list":
                p.list_permissions()
            if args == "map":
                p.map_permissions()

        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Permissions"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_components(args):

        """
        Description: Enumerate components for target APK

        Requirements: Loaded APK

        Usage: permissions
        """

        try:
            from framework.brains.apk.enumeration.components import Components
            c = Components(globals()["apk"])
            c.enum_component()
            
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Components"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_attacksurface(args):

        """
        Description: Enumerates attacksurface for target APK

        Requirements: Loaded APK

        Usage: attacksurface
        """

        try:
            from framework.brains.apk.enumeration.attack_surface import AttackSurface
            c = AttackSurface(globals()["apk"])
            c.enum_attack_surface()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import AttackSurface"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_debuggable(args):

        """
        Description: Make target APK debuggable

        Requirements: Target APK

        Usage: debuggable <name_of_output_directory> && </path/to/apk>
        """

        try:
            from framework.brains.apk.debuggable import Debuggable
            d = Debuggable(args.split()[0], args.split()[1])
            d.do_debuggable()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Debuggable"))
            Logger.do_logger(e.message)

    # dex2jar
    # --------------------
    # d2j
    #

    @staticmethod
    def do_d2j(args):

        """
        Description: Runs d2j-dex2jar.sh on the target APK

        Requirements: Target APK

        Usage: d2j </path/to/apk>
        """

        try:
            from framework.brains.dex2jar.d2j import D2J
            d = D2J(args.split()[0], args.split()[1])
            d.run_d2j()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import D2J"))
            Logger.do_logger(e.message)

    # Bowser
    # --------------------
    # bowser enum, bowser parseUri
    #

    @staticmethod
    def do_bowser(args):

        """
        Description: Runs the bowser toolkit on a target APK

        Requirements: Loaded APK, Lobotomy web services

        Usage: bowser <enum> || <parseUri>
        """

        try:
            from framework.brains.bowser.bowser import Bowser
            b = Bowser(globals()["apks"], globals()["apk"])
            
            if args.split()[0] == "enum":
                b.run_bowser()
            if args.split()[0] == "parseUri":
                b.run_parse_uri()
        
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Bowser"))
            Logger.do_logger(e.message)

    # Dynamic
    # --------------------
    # logcat, instrumentation
    #

    @staticmethod
    def do_logcat(args):

        """
        Description: Runs logcat against the target APK and sends the output
                     to its RESTFul service handler

        Requirements: Loaded APK

        Usage: logcat
        """

        try:
            from framework.brains.dynamic.logcat import Logcat
            l = Logcat()
            l.run_logcat()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Logcat"))
            Logger.do_logger(e.message)

    @staticmethod
    def do_frida(args):

        """
        Description: Runs the Frida instrumentation toolkit against a target process

        Requirements: Loaded APK

        Usage: frida
        """

        try:
            from framework.brains.dynamic.frida.instrumentation import Instrumentation
            i = Instrumentation(globals()["apk"])
            i.do_instrumentation()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + "Unable to import Instrumentation"))
            Logger.do_logger(e.message)
