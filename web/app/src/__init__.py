from flask import Blueprint

# Create Blueprint
# for /src
#
src = Blueprint("src", __name__)

from . import services, views

