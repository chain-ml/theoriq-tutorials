import os
import threading

import dotenv
from flask import Flask
from flask.logging import logging
from theoriq import AgentConfig
from theoriq.extra.flask import theoriq_blueprint

import setup
from logging_config import log_config
from routes import routes, memecoin_twitter
from routes.log_filter import HealthFilter, MetricFilter


logger = logging.getLogger("werkzeug")
log_filters = [HealthFilter(), MetricFilter()]
for log_filter in log_filters:
    logger.addFilter(log_filter)

if __name__ == "__main__":
    app = Flask(__name__)
    log_config()

    # Load agent configuration from env
    dotenv.load_dotenv()
    agent_config = AgentConfig.from_env()

    # Create and register theoriq blueprint
    blueprint = theoriq_blueprint(agent_config, memecoin_twitter)
    app.register_blueprint(blueprint)
    app.register_blueprint(routes)
    logger.info(f"Agent address: {agent_config.address}")
    threading.Thread(target=setup.init).start()

    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5050")), debug=True)
