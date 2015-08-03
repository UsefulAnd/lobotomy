from flask import render_template
from . import src


@src.route("/ui/home")
def home_view():

    return render_template("home.html")


@src.route("/ui/logcat")
def logcat_view():

    """
    Logcat Viewer
    """

    logs = ""

    try:
        with open("app/logs/logcat.log", "r+") as log:
            logs = log.read()
            log.close()
    except IOError as e:
        try:
            # Write Logcat data
            # to logcat.log
            #
            with open("app/logs/flask.log", "w") as log:
                log.write(e.message)
                log.close()

        except IOError:
            # Raise for now
            # until a logger is implemented
            #
            raise

    return render_template("logcat.html", logs=logs)