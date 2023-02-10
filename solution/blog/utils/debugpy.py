import os

import logging

from .constants import Environment

logger = logging.getLogger('blog.utils')


def initialize_debugpy() -> None:
    """
    Injects debugger to running django server.
    Only enabled by setting environment variable ENABLE_DEBUGPY to 'yes'.
    Debugger is available on port 5678.
    This port is also exposed in docker-compose.yml.
    You may connect with for example VSCode, see vscode/launch.json.

    This may be called in wsgi.py if hosting with gunicorn or in manage.py::__main__.
    """
    if os.environ.get('ENABLE_DEBUGPY') == 'yes':
        import debugpy
        # This is okay as long as ENABLE_DEBUGPY only is enabled during development and NOT in production.
        IS_DOCKER = os.environ.get('ENV') == Environment.DOCKER
        HOST = '0.0.0.0' if IS_DOCKER else '0.0.0.0'  # nosec: hardcoded_bind_all_interfaces
        # HOST = '0.0.0.0' if IS_DOCKER else 'localhost'  # nosec: hardcoded_bind_all_interfaces
        host_port = debugpy.listen((HOST, 5678))  # nosec: hardcoded_bind_all_interfaces
        logger.info(f'Attached debugpy on {host_port}')