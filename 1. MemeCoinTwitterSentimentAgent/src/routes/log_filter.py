import logging


class HealthFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        health_endpoint = "/livez" in message or "/readyz" in message
        return not (health_endpoint and "200" in message)


class MetricFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        metric_endpoint = "/metrics" in message
        return not (metric_endpoint and "200" in message)
