# Start project

In this task you will create a django project from scratch.
We will perform these steps inside the container `clean`, through `pipenv`.

Django official documentation:
https://docs.djangoproject.com/en/4.1/

<br>
<hr>
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

To create project (from root of project on host machine):

```
pipenv run django-admin startproject root .
```

</details>

<br>
<br>

## Step 4: Restart servers

You can now exit this container. Docker compose will start it for you.  
Stop the running servers you started earlier with `docker compose up` and rerun the command.  
This time, `clean` should not fail, and will be running on [http://localhost:8001](http://localhost:8001).

<br>
