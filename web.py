import flask
import os
import logging

from flask.helpers import send_from_directory
from flask import Flask

log = logging.getLogger(__name__)

app = Flask(__name__)


class PoGoServer:
    def __init__(self):
        pass

app = Flask(__name__)
pogo_server = PoGoServer()


@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return send_from_directory('views', 'index.html')


@app.route('/resources/<path:path>')
def send_js(path):
    return send_from_directory('resources', path)


@app.route('/api/player')
def api_player():
    res = pogo_server.api.get_player().call()
    data = res['responses']['GET_PLAYER']['player_data']
    return flask.jsonify(data)


@app.route('/api/player/profile')
def api_player_profile():
    res = pogo_server.api.get_player_profile().call()
    data = res['responses']['GET_PLAYER_PROFILE']
    return flask.jsonify(data)


@app.route('/api/inventory')
def api_inventory():
    res = pogo_server.api.get_inventory().call()
    data = res['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']
    return flask.jsonify(data)


@app.route('/api/location')
def api_location():
    lla = pogo_server.api.get_position_raw()
    data = dict()
    data['lat'] = lla[0]
    data['lng'] = lla[1]
    data['alt'] = lla[2]
    return flask.jsonify(data)


@app.route('/api/nearby')
def api_nearby():
    data = pogo_server.api.map_cells or dict()
    return flask.jsonify(data)


@app.route('/api/pokemon_names')
def api_pokemon_names():
    print(pogo_server.api)
    return flask.jsonify(pogo_server.api.pokemon_names)


def start_server(api):
    logging.getLogger("_internal").setLevel(logging.ERROR)  # Silence flask
    port = os.getenv('PORT', 3001)
    pogo_server.api = api
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False, threaded=True)
