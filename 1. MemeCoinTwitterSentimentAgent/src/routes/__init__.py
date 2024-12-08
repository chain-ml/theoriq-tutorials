from flask import Blueprint

routes: Blueprint = Blueprint("routes", __name__)

from .health import livez, readyz
from .metrics import update_endpoint_metrics
from .twitter_semantics import memecoin_twitter
from .log_filter import HealthFilter, MetricFilter
