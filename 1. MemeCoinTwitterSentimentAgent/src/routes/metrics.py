from time import time
from flask import Response
from prometheus_client import generate_latest, Counter, Summary

from . import routes

counter = Counter(
    "agent_http_requests_total", "HTTP requests", ["method", "endpoint", "status"]
)

summary = Summary(
    "agent_http_requests_duration",
    "Duration of HTTP requests in ms",
    ["method", "endpoint", "status"],
)


def update_endpoint_metrics(method: str, endpoint: str, status: int, start_time: float):
    duration = time() - start_time
    summary.labels(method=method, endpoint=endpoint, status=status).observe(
        duration * 1000
    )
    counter.labels(method=method, endpoint=endpoint, status=status).inc()


@routes.route("/metrics", methods=["GET"])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
