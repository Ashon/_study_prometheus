import logging
import sys

from flask import Flask
from flask import current_app
from flask import jsonify
from flask import request

LOGGER_FORMAT = (
    '[%(asctime)s] [pid:%(process)s, %(levelname)s]'
    '%(module)s:%(funcName)s - %(message)s'
)


def bypass_alert():
    current_app.logger.info(request.json)
    return jsonify(request.json)


def get_application():
    app = Flask('alertreceiver')

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOGGER_FORMAT)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.route('/alert/prometheus', methods=['POST'])(bypass_alert)

    return app


if __name__ == '__main__':
    get_application().run(host='0.0.0.0', debug=True)
