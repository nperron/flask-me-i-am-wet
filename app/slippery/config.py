import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    VAR_DEV_ONLY = 'I am a dev env'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    VAR_TEST_ONLY = 'I am a test env'

config = {
    "development": "slippery.config.DevelopmentConfig",
    "testing": "slippery.config.TestingConfig",
    "default": "slippery.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name]) # object-based default configuration
    app.config.from_pyfile("config.py", silent=True) # instance-folders configuration
