# imports
from rest_framework import routers

from django.urls import path, include

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from . import views
# End: imports -----------------------------------------------------------------

app_name = 'blog'

router = routers.DefaultRouter()
# router.register('events', views.EventView, 'events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_framework/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
]

# Setup static access and media upload
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
