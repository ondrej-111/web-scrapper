import os
import firebase_admin
import flask
from flask import request, abort, jsonify
from helpers.helpers import google_search_crawlera, get_first_result
from helpers.Config import Config


app = flask.Flask(__name__)

firebase_admin.initialize_app()
Config(os.getenv('FLASK_ENV') or 'prod')


@app.route('/api/search', methods=['POST'])
def google_search():
    # get the google search first result
    request_json = request.json
    query = request_json.get('query', None)
    if query is None:
        abort(409, 'Input must contains query parameter.')

    # proxy = get_random_proxy()
    result = google_search_crawlera(query)
    if result.status_code != 200:
        abort(409, 'Proxy not work')
    url = get_first_result(result.text)
    return jsonify({'url': url})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
