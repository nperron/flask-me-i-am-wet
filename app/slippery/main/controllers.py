from flask import Blueprint
from flask import current_app as app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    for key in app.config:
        print("\t%s => %s" % (key, app.config[key]))
    return "Slippery index API"
