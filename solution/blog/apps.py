import os
import logging

from django.apps import AppConfig
from django.conf import settings

LOG = logging.getLogger('blog')


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self) -> None:
        from . import signals  # noqa: F401
        from .models import User

        if settings.DEBUG:
            try:
                username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
                password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
                email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
                LOG.info(f"Attempt to create superuser '{username}'")
                User.objects.create_superuser(username=username, password=password, email=email)
            except Exception as e:
                LOG.info(e)
