# from rest_framework import serializers
"""
In this module we can define serializers for rest-framework.

Serializers transform model instances into json.
"""

from rest_framework import serializers

from blog.models import Author, BlogPost


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'
