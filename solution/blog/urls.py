# imports
from rest_framework import routers

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from . import views
# End: imports -----------------------------------------------------------------

app_name = 'blog'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('test/', views.TestView.as_view()),
]

# Setup static access and media upload
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
