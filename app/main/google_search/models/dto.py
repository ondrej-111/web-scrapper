from flask_restplus import Namespace, fields


class SearchResultDto:
    ns = Namespace('search', description='Search for first result from google search engine')
    user_auth = ns.model('query', {
        'url': fields.String(required=True, description='result url'),
    })
