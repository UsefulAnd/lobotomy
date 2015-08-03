#!/usr/bin/env python

from app import create_app
from flask.ext.script import Manager, Shell

app = create_app()
manager = Manager(app)


def make_shell_content():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_content()))

if __name__ == "__main__":

    # python run.py runserver -h 0.0.0.0
    # python run.py shell
    #
    manager.run()