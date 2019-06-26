from flask_restplus import Api
from flask import Blueprint

from app.main.google_search.controllers.google_search_controller import ns as google_search_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='First result from Google',
          version='1.0',
          description='Flask api to return first result from Google search engine.'
          )

api.add_namespace(google_search_ns, path='/search')
