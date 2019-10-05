import os
from flask_script import Manager

from app import blueprint
from app.main import create_app

app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()
app.config['RESTPLUS_VALIDATE'] = True

manager = Manager(app)

if __name__ == "__main__":
    app.run()
