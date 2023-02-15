# imports
from rest_framework import routers

from django.urls import path, include

from . import views
# End: imports -----------------------------------------------------------------

app_name = 'blog'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
