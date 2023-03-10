from rest_framework.viewsets import ModelViewSet

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.shortcuts import render

from blog.models import Author, BlogPost, User
from blog.serializers import AuthorSerializer, BlogPostSerializer


class JsonView(View):
    """Simple view to return json data."""

    def get(self, request: HttpRequest) -> JsonResponse:
        data = {'test': 123}
        return JsonResponse(data=data)


class HelloView(View):
    """Simple hello-world view."""

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('Hello World!')


class AllBlogPostsView(View):
    """View to display all BlogPosts with template."""

    template_name = 'blog/all_blogposts.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        blog_posts = BlogPost.objects.all()
        return render(request, self.template_name, {'blog_posts': blog_posts})


class PermissionTestView(View):

    def get(self, request: HttpRequest, username: str) -> JsonResponse:
        user = User.objects.get(username=username)
        can_delete = user.has_perm('blog.delete_blogpost')
        can_change = user.has_perm('blog.change_blogpost')
        data = {
            'can_delete': can_delete,
            'can_change': can_change,
        }
        return JsonResponse(data=data)


class AuthorViewSet(ModelViewSet):
    """REST api viewset for Author."""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BlogPostViewSet(ModelViewSet):
    """REST api viewset for Author."""
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
