# Blog application

In this task you will be the architect of the backend for a blog application.

> Prerequisites:
> You need a working django project, see task [Start project](startproject.md).

<br>

Table of content:

- [Step 1: Initialize application](#step-1-initialize-application)
- [Step 2: Add app to project](#step-2-add-app-to-project)
- [Step 3: Create model](#step-3-create-model)
- [Bonus 1: Modify behaviour on save](#bonus-1-modify-behaviour-on-save)

<br>
<hr>
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


class Blog(models.Model):
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
