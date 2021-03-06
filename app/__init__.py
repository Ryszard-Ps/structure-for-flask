# -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import configparser
from logging.handlers import RotatingFileHandler
from flask_cors import CORS

db = SQLAlchemy()


def create_app(config_filename):
    # Here we  create flask instance
    app = Flask(__name__)

    # Allow cross-domain access to API.
    #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Load the default configuration
    app.config.from_object(config_filename)

    # Load the configuration from the instance folder
    # app.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    # *app.config.from_envvar('APP_CONFIG_FILE')

    # Configure logging.
    configure_logging(app)

    # Configure Database
    db.init_app(app)

    # Init modules
    init_modules(app)

    return app

def configure_logging(app):
    ''' Configure the app's logging.
     param app: The Flask app object
    '''

    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # If path directory doesn't exist, create it.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create and register the log file handler.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    # First log informs where we are logging to.
    # Bit silly but serves  as a confirmation that logging works.
    app.logger.info('Logging to: %s', log_path)


def init_modules(app):

    # Import blueprint modules
    from app.home.views import home
    from app.api.v1.views import v1

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(v1, url_prefix='/api/v1')
