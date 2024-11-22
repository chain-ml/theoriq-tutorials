import logging
from flask import jsonify

import setup

from . import routes

logger = logging.getLogger(__name__)


@routes.route("/livez", methods=["GET"])
def livez():
    logging.info('message="Received /livez request"')
    resp = jsonify(livez=setup.is_live)
    resp.status_code = 200 if setup.is_live else 503
    return resp


@routes.route("/readyz", methods=["GET"])
def readyz():
    logging.info('message="Received /readyz request"')
    resp = jsonify(readyz=setup.is_ready)
    resp.status_code = 200 if setup.is_ready else 503
    return resp
