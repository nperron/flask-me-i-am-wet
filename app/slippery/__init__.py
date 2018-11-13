from flask import Flask
from slippery.main.controllers import main
from slippery.admin.controllers import admin

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
