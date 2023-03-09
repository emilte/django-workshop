# imports
from rest_framework import routers

from django.urls import path, include

from . import views
# End: imports -----------------------------------------------------------------

app_name = 'blog'

router = routers.DefaultRouter()
router.register('author', views.AuthorViewSet)
router.register('blog-post', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('json/', views.JsonView.as_view()),
    path('hello/', views.HelloView.as_view()),
    path('all/', views.AllBlogPostsView.as_view()),
    path('user/<str:username>/', views.PermissionTestView.as_view()),
]
