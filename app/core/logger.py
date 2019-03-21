import sys
import logging
import os
from datetime import datetime
import inspect

class Logger():
    _default_logger = None
    _PREFIX = ""
    #_sentry_client = Client(Config.get('sentry', 'dsn'), release="1.0.0")

    def __init__(self, prefix=None):
        if Logger._default_logger is None:
            dir_path = "logs/"
            Logger._default_logger = logging.getLogger("custom")
            Logger._default_logger.setLevel(logging.DEBUG)

            stdout_handler = logging.StreamHandler(sys.stdout)
            Logger._default_logger.addHandler(stdout_handler)

        if prefix is not None:
            Logger._PREFIX = prefix

    def _get_default_logger(self):
        if Logger._default_logger is None:
            raise Exception("Logger not initialized")
        else:
            return Logger._default_logger

    def info(self, log, *args, **kwargs):
        self._get_default_logger().info(log, *args, **kwargs)

    def debug(self, log, *args, **kwargs):
        caller_info = inspect.stack()[1]
        caller_info_format = "%s:%s" % (caller_info.filename, caller_info.lineno)
        formatted_log = "[%s] |DEBUG| - %s: %s" % (self._time(), caller_info_format, log)
        self._get_default_logger().debug(formatted_log, *args, **kwargs)

    def error(self, log, *args, **kwargs):
        caller_info = inspect.stack()[1]
        caller_info_format = "%s:%s" % (caller_info.filename, caller_info.lineno)
        formatted_log = "[%s] |ERROR| - %s: %s" % (self._time(), caller_info_format, log)
        self._get_default_logger().error(formatted_log, *args, **kwargs)

    def _time(self):
        now = datetime.utcnow()
        return now.strftime("%Y-%m-%d %H:%M:%S")