import os
import firebase_admin
import flask
from flask import request, abort, jsonify, make_response
from helpers.helpers import google_search_crawlera, get_first_result, get_bool
from helpers.Config import Config

app = flask.Flask(__name__)

firebase_admin.initialize_app()
config = Config(os.getenv('FLASK_ENV') or 'prod')


@app.route('/api/search', methods=['POST'])
def google_search():
    # get the google search first result

    request_json = None
    try:
        request_json = request.json
    except:
        abort(make_response(jsonify(message='Body is required.'), 400))

    query = request_json.get('query', None)
    if query is None:
        abort(make_response(jsonify(message='Input must contains query parameter.'), 409))

    result = google_search_crawlera(query)
    if result.status_code != 200:
        abort(make_response(jsonify(message='Proxy not work'), 409))
    url = get_first_result(result.text)
    return jsonify({'url': url})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=get_bool(config.get('DEFAULT', 'debug')))
