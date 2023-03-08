/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Django REST framework](rest.md)

# Task: Django REST framework

In this task you will create a rest api for a model.
You can also protect the endpoint behind authentication.

> Prerequisites:
> You should probably do the [blog](blog.md) task before doing this.
> You need a model to provide a rest api for it.
> If you want to proceed without the blog task, create a model in step 0.

<br>
<br>

Table of contents:

- [Step 0: Create a model](#step-0-create-a-model)
- [Step 1: Install djangorestframework](#step-1-install-djangorestframework)
- [Step 2: Create a ModelSerializer](#step-2-create-a-modelserializer)
- [Step 3: Create a ModelViewSet](#step-3-create-a-modelviewset)
- [Step 4: Create an endpoint](#step-4-create-an-endpoint)

<br>
<hr>
<br>

## Step 0: Create a model

> Only needed if you haven't made a model yet.

Create a model with at least one field.

<details>
<summary>Solution</summary>

See [official documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/)

```py
# blog/models.py

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    hidden = models.BooleanField()
```

</details>

<br>
<br>

## Step 1: Install djangorestframework

https://www.django-rest-framework.org/tutorial/1-serialization/#setting-up-a-new-environment

Install and setup `rest_framework` in your project.

<details>
<summary>Solution</summary>

To install (from root of project on host machine):

```
docker compose exec clean pipenv install djangorestframework
```

Register the new app in django.

```py
# root/settings.py

INSTALLED_APPS = [
    ...
    'rest_framework', # <-- Add this.
]
```

</details>

<br>
<br>

## Step 2: Create a ModelSerializer

This is a class that can transform models (python objects) retrieved from the database.
It will create data as json, ready to send back as an http response.

In it's simplest form, allow all fields.

See [ModelSerializer](https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers)

<details>
<summary>Solution</summary>

```py
# blog/serializers.py

from rest_framework import serializers

from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'
```

</details>

<br>
<br>

## Step 3: Create a ModelViewSet

This is a class that provides all CRUD operations on a model with minimal effort.

Create a view for your model in file `blog/views.py`.
Attributes to specify:

- `serializer_class`
- `queryset`

See [ModelViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)

<details>
<summary>Solution</summary>

```py
# blog/views.py

from rest_framework.viewsets import ModelViewSet

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

class BlogPostViewSet(ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
```

</details>

<br>
<br>

## Step 4: Create an endpoint

You haven't made an url to use the api yet.

In [blog](/clean/root/settings.py) you can see that the setting `ROOT_URLCONF` says the file [/root/urls.py](/clean/root/urls.py) is the main entrypoint when receiving a request.  
Make sure to forward all traffic beginning with `/blog/` to your app.  
(Hint: read the docstring in [/root/urls.py](/clean/root/urls.py))

Afterwards create a path for your api `BlogPostViewSet` in `blog/urls.py`.  
See: https://www.django-rest-framework.org/api-guide/routers/#usage

<details>
<summary>Solution</summary>

```py
# blog/urls.py

from rest_framework import routers
from .views import BlogPostViewSet

router = routers.SimpleRouter()

router.register('blog-post', BlogPostViewSet)

# The variable 'urlpatterns' is recognised by django.
urlpatterns = router.urls

```

</details>

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
