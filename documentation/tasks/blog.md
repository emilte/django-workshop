/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Blog application](blog.md)

# Task: Blog application

In this task you will be the architect of a blog application.

> Prerequisites:
> You need a working django project, see task [Start project](startproject.md).

<br>

Table of contents:

- [Step 1: Initialize application](#step-1-initialize-application)
- [Step 2: Add app to project](#step-2-add-app-to-project)
- [Step 3: Create model](#step-3-create-model)
- [Step 4: Connect the Django admin site to the models](#step-4-connect-the-django-admin-site-to-the-models)
- [Step 5: Create views for displaying content](#step-5-create-views-for-displaying-content)
- [Step 6: Mapping URLs to views](#step-6-mapping-urls-to-views)
- [Step 7: Display blog posts](#step-7-display-blog-posts)
- [Bonus 1: Modify behaviour on save](#bonus-1-modify-behaviour-on-save)

<br>
<br>

## Step 1: Initialize application

Run a django command to start an app with the name `'blog'`.

Resource: https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-the-polls-app

<details>
<summary>Solution</summary>

To create app (from root of project on host machine):

```
docker compose exec clean pipenv run python manage.py startapp blog
```

</details>

<br>
<br>

## Step 2: Add app to project

Our new app is only a collection of files, they don't do very much at the moment.  
Django isn't aware of them yet.  
Tell your django project to add `blog` as an app.

Hint:
<br>
See `INSTALLED_APPS` in `root/settings.py`.

<details>
<summary>Solution</summary>

https://docs.djangoproject.com/en/4.1/intro/tutorial02/#activating-models

```py
INSTALLED_APPS = [
    ...
    'blog', # <-- Add this.
]
```

</details>

<br>
<br>

## Step 3: Create model

Create a model for `BlogPost`.  
Be creative, identify fields you find relevant to a blogpost.  
To get you started -- you should probably have a `title`, and maybe an `author`.

Bonus:
You can create more models to achieve relations.

Resource: https://docs.djangoproject.com/en/4.1/topics/db/models/

<details>
<summary>Solution</summary>

> `blank`: Specifies if field can be blank when creating an instance.  
> `null`: Specifies a database constraint field can be blank when creating an instance.

```py
# blog/models.py

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=42, blank=True, null=True)
    last_name = models.CharField(max_length=42, blank=True, null=True)
    born = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        """
        Returns the string representation of an instance.
        We want to see the full name (strip whitespace if partially missing name)
        """
        return f'{self.last_name} {self.last_name}'.strip()


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    text = models.TextField(blank=False, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
    published = models.DateTimeField()
    hidden = models.BooleanField(default=False)

    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Returns the string representation of an instance.
        We want to see the title.
        """
        return f'{self.title}'
```

</details>

<br>
<br>
    
## Step 4: Connect the Django admin site to the models
The admin site is an interface accessible to users with a username and password, that can be used to manage the content on the site. To log into the admin site and access all functionality you should have created a superuser in a previous step (see [startproject](/documentation/tasks/startproject.md#step-5-create-a-superuser)).

Resource: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/

First enter https://localhost:8001/admin/ and log in using the username and password you have defined. This will show the Django admin site/panel, but it does not contain any information on the models you have created yet. To connect the models you defined in blog/models.py register the models in `blog/admin.py` as described in the resource-link.

<details>
<summary>Solution</summary>

```py
# blog/admin.py

from django.contrib import admin
from blog.models import Author, BlogPost

# Register your models here.
admin.site.register(Author)
admin.site.register(BlogPost)
```

</details>
    
After registering the models you can re-enter the admin site. It should now be possible to add an author or write a new blog post based on the models you created.

<br>
<br>

## Step 5: Create views for displaying content

In this section you will create a view in order to display content. Views can be function-based or class-based, in this workshop the latter is used. You can read more about the two approaches in the resource link. A view takes a web request and returns a web response, which for example can be the html content on your page.

Resource: https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/#using-class-based-views

Write a view called `Home` that can be used to display some text of your choice.

<details>

<summary>Solution</summary>

```py
# blog/views.py

from django.http import HttpResponse, HttpRequest
from django.views import View

class Home(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('Welcome to my blog!')

```

</details>

<br>
<br>

## Step 6: Mapping URLs to views

You now have a view that contains a http response which includes something you want to display. To display this view at a particular URL, you'll need to create a URLconf which is a mapping between URL path expressions and Python functions (your views). Use the given resources, as well as the comments in root/urls.py and blog/urls.py to map between the URLs and views.

Resource: https://docs.djangoproject.com/en/4.1/topics/http/urls/

<details>
<summary>Solution</summary>

```py
# blog/urls.py
from django.urls import path

from blog.views import Home

urlpatterns = [
    path('all/', Home.as_view(), name='home'),
]
```

```py
# root/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

```

</details>

Now you can enter https://localhost:8001/blog/all/.

<br>
<hr>
<br>

## Step 7: Display blog posts

The content you displayed in the previous view isn't particularly interesting.

![We want to see all the blogposts!](/documentation/images/blogposts.jpg)

To display the blog posts, you can render an html page instead.  
Luckily, Django has a built in template system.  
You need to:

- Create an HTML-file `blog/templates/blog/home.html` and use it in your View.
- Fetch all BlogPosts and give them as context to the template.
- Loop over each blogpost and render them.

Resources:

- https://docs.djangoproject.com/en/4.1/intro/tutorial03/#use-the-template-system
- https://docs.djangoproject.com/en/4.1/topics/db/queries/#retrieving-all-objects

<details>
<summary>Solution</summary>

```py
# blog/views.py

from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render

from blog.models import BlogPost

class Home(View):
    template_name: str = 'blog/home.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        # Fetch all BlogPosts.
        blog_posts = BlogPost.objects.all()
        # Give the results as context to template with name 'blog_posts'.
        return render(request, self.template_name, {'blog_posts': blog_posts})
```

</details>

<br>

<details>
<summary>Solution</summary>

```html
<!-- > blog/templates/blog/home.html -->

<div>
  <h1>Django Blog</h1>
  <p>Welcome to my super cool blog written in Django!</p>
</div>

<div>
  {% for blog_post in blog_posts %}
  <div>
    <h2>{{ blog_post.title }}</h2>
    <p>{{ blog_post.text }}</p>
  </div>
  {% endfor %}
</div>
```

</details>

<br>
<hr>
<br>

## Bonus 1: Modify behaviour on save

If an author has `last_name` equal to `'Nordmann'`, change it to `'Viking'`.

See this post:
https://www.geeksforgeeks.org/overriding-the-save-method-django-models/

<details>
<summary>Solution</summary>

```py
# blog/models.py

from django.db import models

class Author(models.Model):
    ...

    def save(self, *args, **kwargs) -> None:

        # Modify name.
        if self.last_name == 'Nordmann':
            self.last_name = 'Viking'

        # Proceed with saving.
        super().save(*args, **kwargs)
```

</details>

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
