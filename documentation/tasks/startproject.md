# Start project

In this task you will create a django project from scratch.
We will perform these steps inside the container `clean`, through `pipenv`.

Django official documentation:
https://docs.djangoproject.com/en/4.1/

<br>
<hr>
<br>

## Step 1: Install django

Install django through `pipenv` inside the container `clean`.

See [Useful commands](../useful-commands.md)

<details>
<summary>Solution</summary>

To create app (from root of project on host machine):

```
docker compose exec clean pipenv run python manage.py startapp blog
```

</details>

<br>
<br>

## Step 2: Start project

Start a new project with the name `root` in the current directory (use a single dot `.`).

Resource: https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-a-project

<details>
<summary>Solution</summary>

To create project (from root of project on host machine):

```
docker compose exec clean pipenv run python manage.py startapp blog
```

</details>

<br>
