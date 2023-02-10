class Environment:
    """
    Useful in eg. templates.
    Override in different settings.
    """
    DEV = 'development'
    PROD = 'production'
    DOCKER = 'docker'

    ALL = [DEV, PROD, DOCKER]


# Name of exposed csrf-token header in http traffic.
XCSRFTOKEN = 'X-CSRFToken'
