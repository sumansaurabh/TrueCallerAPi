import logging
import os


class Config(object):
    """Config object for the Project"""

    TRUECALLER_SEARCH_URL = "http://www.truecaller.com/"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    YAHOO_USERNAME = os.environ['YAHOO_USERNAME']
    YAHOO_PASSWORD = os.environ['YAHOO_PASSWORD']
    LOGGING = logging.INFO


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
