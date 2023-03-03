/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Start project](startproject.md)

# Start project

In this task you will create a django project from scratch.
We will perform these steps inside the container `clean`, through `pipenv`.

Django official documentation:
https://docs.djangoproject.com/en/4.1/

<br>
<br>

Table of contents:

- [Step 1: Enter the container](#step-1-enter-the-container)
- [Step 2: Install django](#step-2-install-django)
- [Step 3: Start project](#step-3-start-project)
- [Step 4: Restart servers](#step-4-restart-servers)
- [Step 5: Create a superuser](#step-5-create-a-superuser)

<br>
<br>

## Step 1: Enter the container

Start a shell (bash) within container clean.

See [Useful commands](../useful-commands.md)

<details>
<summary>Solution</summary>

To enter container (from root of project on host machine):

```
docker compose run clean bash
```

</details>

<br>
<br>

## Step 2: Install django

Install django through `pipenv` inside the container `clean`.  
This container has `pipenv` installed already.

See [Useful commands](../useful-commands.md)

<details>
<summary>Solution</summary>

```
pipenv install django
```

</details>

<br>
<br>

## Step 3: Start project

Start a new project with the name `root` in the current directory (use a single dot `.`).

Resource: https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-a-project

<details>
<summary>Solution</summary>

```
pipenv run django-admin startproject root .
```

> `django-admin` is only needed before starting a project.  
> It created a file named `manage.py` which we will use from now on.

</details>

<br>
<br>

## Step 4: Restart servers

You can now exit this container. Docker compose will start it for you.  
Stop the running servers you started earlier with `docker compose up` and re-run the command.  
This time, `clean` should not fail, and will be running on [http://localhost:8001](http://localhost:8001).

<br>
<br>

## Step 5: Create a superuser

Django comes with a builtin admin-panel. To login after you restart the server, you first need a user.  
Create a new user through `manage.py`.

See [Useful commands](../useful-commands.md)

Afterwards you may visit the admin-panel on [http://localhost:8001/admin](http://localhost:8001/admin).

<details>
<summary>Solution</summary>

From root of project on host machine:  
Run and follow the instructions.

```
docker compose exec clean pipenv run python manage.py createsuperuser
```

</details>

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
