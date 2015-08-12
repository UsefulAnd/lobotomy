import frida
import sys
from framework.logging.logger import Logger
from subprocess import Popen
from datetime import datetime
from blessings import Terminal
t = Terminal()


class Instrumentation(object):
    def __init__(self, apk):

        super(Instrumentation, self).__init__()
        self.apk = apk

    @staticmethod
    def on_message(message, data):

        if message:
            print(t.green("[{0}] ".format(datetime.now())) + message["payload"])

    @staticmethod
    def do_webview():

        """
        Instrument calls made to WebViews - loadUrl(), addJavascriptInterface()
        """

        web_view = """

        Dalvik.perform(function () {

            var WebView = Dalvik.use("android.webkit.WebView");
            var WebViewClient = Dalvik.use("android.webkit.WebViewClient");

            WebView.loadUrl.overload("java.lang.String").implementation = function (s) {

                send("loadUrl()");

                this.loadUrl.overload("java.lang.String").call(this, s);

            };

            WebView.addJavascriptInterface.implementation = function (o, s) {

                send("addJavascriptInterface()");

                this.addJavascriptInterface(o, s);
            };

            WebViewClient.shouldOverrideUrlLoading.implement = function (o, s) {


                send("shouldOverrideUrlLoading()");
                send(s.toString());

                this.shouldOverrideUrlLoading(o, s);

            };

        });

        """

        return web_view

    @staticmethod
    def do_activities():

        """
        Instrument calls made to activities - onCreate(), onNewIntent()
        """

        activities = """

        Dalvik.perform(function () {

            var Activity = Dalvik.use("android.app.Activity");
            var Intent = Dalvik.use("android.content.Intent");

            Activity.onNewIntent.implementation = function (i) {

                var intent = Dalvik.cast(i, Intent);
                action = intent.getAction();
                component = intent.getComponent();
                extras = intent.getExtras();

                send("onNewIntent()");
                send(component.toString());
                send(action.toString());

                if(extras) {
                                send("Found extras!");
                            }

                this.onNewIntent(i);
            };

            Activity.onCreate.implementation = function (b) {

                currentActivity = this.getComponentName();

                send("onCreate()");
                send(currentActivity.toString());

                this.onCreate(b);
            };

        });

        """

        return activities

    def run_instrumentation(self):

        """
        Select and run instrumentation function using the
        Frida instrumentation toolkit
        """

        while True:
            print(t.green("[{0}] ".format(datetime.now()) +
                          t.cyan("Enter 'quit' to exit Frida module!")))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Available Frida functions: ") +
                          "activities, webview"))

            function = raw_input(t.green("[{0}] ".format(datetime.now())
                                         + t.yellow("Enter Frida function: ")))

            if function == "quit":
                break

            try:
                if function == "activities":
                    # adb forward just
                    # in case
                    #
                    Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
                    process = frida.get_device_manager().enumerate_devices()[-1].attach(self.apk.get_package())
                    script = process.create_script(self.do_activities())
                    script.on('message', self.on_message)
                    script.load()
                    sys.stdin.read()

                elif function == "webview":
                    # adb forward just
                    # in case
                    #
                    Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
                    process = frida.get_device_manager().enumerate_devices()[-1].attach(self.apk.get_package())
                    script = process.create_script(self.do_webview())
                    script.on('message', self.on_message)
                    script.load()
                    sys.stdin.read()

            except frida.ProcessNotFoundError as e:
                print(t.red("[{0}] ".format(datetime.now()) +
                            "Could not connect to target process!"))
                Logger.run_logger(e.message)
            except frida.ServerNotRunningError as e:
                print(t.red("[{0}] ".format(datetime.now()) +
                            "The frida-server is not running!"))
                Logger.run_logger(e.message)
            except frida.TransportError as e:
                print(t.red("[{0}] ".format(datetime.now()) +
                            "Connection was closed!"))
                Logger.run_logger(e.message)
            except KeyboardInterrupt:
                pass
