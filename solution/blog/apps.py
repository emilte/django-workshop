import os
import logging

from django.apps import AppConfig
from django.conf import settings

LOG = logging.getLogger('blog')


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self) -> None:
        from . import signals
        from django.core import management

        if settings.DEBUG:
            try:
                LOG.info(f"Attempt to create superuser '{os.environ.get('DJANGO_SUPERUSER_USERNAME')}'")
                management.call_command('createsuperuser', interactive=False)
            except Exception as e:
                LOG.info(e)
