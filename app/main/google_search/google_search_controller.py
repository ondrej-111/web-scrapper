from flask import request, abort
from flask_restplus import Resource

from .models.dto import SearchResultDto

api = SearchResultDto.api


@api.route('')
class GoogleSearch(Resource):
    """
        Google search first occur.
    """

    @api.doc('search')
    def post(self):
        # get the google search first result
        request_json = request.json
        if request_json.get('query', None) is None:
            abort(409, 'Input must contains query parameter.')
        return {'url': request_json['query']}
