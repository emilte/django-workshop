# django-workshop

Hi, and welcome to my workshop!

In this workshop, you will learn the basics of Django, and lots of other treats the python environment can provide.

Before we can start though, I need you to do something for me. You see, there are some tools I cannot install for you. Please take a look at the list in [prerequisites](#prerequisites) below and install the required tools 🔧

<br>
<br>

## Prerequisites

See [prerequisites](/documentation/prerequisites.md).

<br>
<br>

## Setup

### 1. Locate directory you want to clone project.

```
git clone git@github.com:emilte/django-workshop.git;
```

<br>
<br>

### 2. Copy environment files.

```
cp .vscode/settings.default.json .vscode/settings.json
cp clean/.docker.example.env clean/.docker.env
cp solution/.docker.example.env solution/.docker.env
```

<br>
<br>

### 3. Build project

```
docker compose build
```

<br>
<br>

### 4. Run project for initial setup

It's expected to display errors for `clean` container.
This is the container you are about to create a django project inside.

```
docker compose up
```

The `solution` server is now running on [http://localhost:8002](http://localhost:8002).  
You may browse the admin panel on [http://localhost:8002](http://localhost:8002).
Credentials can be found in [solution/.docker.env](/solution/.docker.env)

<br>
<br>

### 5. Install dependencies (optional)

This step is only to enhance the VSCode experience where it can recognise Django, enable formatter, linters etc...

```
cd solution
```

> `pipenv` will recognise dependencies automatically from [Pipfile](/solution/Pipfile).
> `PIPENV_VENV_IN_PROJECT=1` will ensure that the environment is installed within this folder.

```
PIPENV_VENV_IN_PROJECT=1 pyenv exec python -m pipenv install
```

If you want to try again, you can remove the environment with:

```
pyenv exec python -m pipenv --rm
```

<br>
<br>

### 6. Select interpreter in VSCode

`Cmd + Shift + P` --> `Select interpreter` --> `+ Enter interpreter path`

Write `solution/.venv` and hit `Enter`.

<br>
<br>

## Documentation

Go to [documentation](/documentation/README.md) to continue with workshop.
