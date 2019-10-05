from flask import Flask
from flask_bcrypt import Bcrypt
from base.Config import Config
from base.helpers import get_bool

flask_bcrypt = Bcrypt()


def create_app(env):
    Config(env)
    app = Flask(__name__)
    # config settings
    debug = get_bool(Config.get('DEFAULT', 'debug'))
    app.config['DEBUG'] = debug
    flask_bcrypt.init_app(app)

    return app