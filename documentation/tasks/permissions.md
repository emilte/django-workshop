/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Permissions](security.md)

# Task: Permissions

Django comes with a powerful permission system out of the box.

Resources:

- https://docs.djangoproject.com/en/4.1/topics/auth/default/
- https://testdriven.io/blog/django-permissions/

<br>
<br>

Table of contents:

- [Step 1: Register Permission](#step-1-register-permission)
- [Step 2: Assign permissions](#step-2-assign-permissions)
- [Step 3: Check permissions](#step-3-check-permissions)
- [Bonus 1: Custom permission](#bonus-1-custom-permission)

<br>
<br>

## Step 1: Register Permission

Django autogenerates permissions for all models in the database.  
To get an overview, we can register the model `Permission` in the admin panel.

<details>
<summary>Solution</summary>

```py
# blog/admin.py

from django.contrib import admin
from django.contrib.auth.models import Permission

admin.site.register(Permission)
```

</details>

<br>
<br>

## Step 2: Assign permissions

Because you as a superuser have all permissions, create a new plain user you can use for testing.

Try to assign at least one user permission and one group permission on this user.

<details>
<summary>Solution</summary>

![Browse admin panel](/documentation/images/browse_admin.jpg)

</details>

<br>
<br>

## Step 3: Check permissions

Create a simple view where you return a json response containing the boolean result for both permissions in [Step 2](#step-2-assign-permissions).

See solution: http://localhost:8002/user/`<username>/`  
(replace username with credentials from [solution/.docker.env](/solution/.docker.env))

Hint:  
The `User` object in Django is equipped with methods to check permissions, e.g. `.has_perm(...)`.  
A permission is identified as a string on the format `<app_name>.<code_name>`.

Django generates 4 basic/common permissions per model for us: `create_*`, `change_*`, `view_*`, `delete_*`.

Example:

```py
some_user.has_perm('blog.delete_blogpost')
```

<details>
<summary>Solution</summary>

```py
# blog/urls.py
from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path('user/<str:username>/', views.PermissionTestView.as_view()),
]
```

```py
# blog/views.py

from rest_framework.viewsets import ModelViewSet

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth.models import User


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
```

</details>

<br>
<hr>
<br>

## Bonus 1: Custom permission

Say you are in the middle of developing a new feature, why not create a custom permission to use this feature?

Imagine that each BlogPost can contain a video, use the Metaclass on BlogPost to enable feature-toggling.  
Add another check to the view you created in [Step 3](#step-3-check-permissions).

Resource: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-permissions

Hint:  
Restart the server to let docker update permissions in the database with `makemigrations` and `migrations`.

<details>
<summary>Solution</summary>

```py
# blog/models.py

from django.db import models

class BlogPost(models.Model):
    ...

    class Meta:
        permission = [
            ('feature_video_blogpost', 'Can use video feature on BlogPost'),
        ]
```

</details>

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
