from flask_script import Manager
from base.helpers import parse_input_args

from app import blueprint
from app.main import create_app

args = parse_input_args()

app = create_app(args['env'])
app.register_blueprint(blueprint)

app.app_context().push()
app.config['RESTPLUS_VALIDATE'] = True

manager = Manager(app)

app.run()
# @manager.command
# def run():
#     app.run()


if __name__ == '__main__':
    manager.run()