from flask import request, abort
from flask_restplus import Resource
from ..helpers.helpers import google_search, get_first_result, get_random_proxy

from app.main.google_search.models.dto import SearchResultDto

ns = SearchResultDto.ns


@ns.route('')
class GoogleSearch(Resource):
    """
        Google search first occur.
    """

    @ns.doc('search')
    def post(self):
        # get the google search first result
        request_json = request.json
        query = request_json.get('query', None)
        if query is None:
            abort(409, 'Input must contains query parameter.')

        proxy = get_random_proxy()
        result = google_search(query, proxy)
        if result.status_code != 200:
            abort(409, 'Proxy not work')
        url = get_first_result(result.text)
        return {'url': url}
