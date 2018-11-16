from flask import Flask
from slippery.main.controllers import main
from slippery.admin.controllers import admin
from slippery.config import configure_app

app = Flask(__name__, instance_relative_config=True)

configure_app(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
