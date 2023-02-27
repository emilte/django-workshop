# django-workshop

Hi, and welcome to my workshop! 😊

In this workshop, you will learn the basics of Django, and lots of other treats the python environment can provide.

Before we can start though, I need you to do something for me. You see, there are some tools I cannot install for you 😔 Please take a look at the list in [prerequisites](#prerequisites) and install the required tools 🔧
The project was made primarily to run in docker, but is compatible with local setup aswell.

<br>
<hr>
<br>

## Table of contents:

- [Table of contents:](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Step 1: Clone project](#step-1-clone-project)
  - [Step 2: Copy environment files](#step-2-copy-environment-files)
  - [Step 3: Run project](#step-3-run-project)
  - [Step 4: Install dependencies (optional)](#step-4-install-dependencies-optional)
  - [Step 5: Select interpreter in VSCode](#step-5-select-interpreter-in-vscode)
- [Documentation](#documentation)

<br>
<hr>
<br>

## Prerequisites

See [prerequisites](/documentation/prerequisites.md).

<br>
<br>

## Setup

### Step 1: Clone project

Locate directory you want to have the project, clone the project and navigate into it.

```
git clone git@github.com:emilte/django-workshop.git && cd django-workshop
```

<br>
<br>

### Step 2: Copy environment files

These files configure the environment the code runs in.  
After running these commands, I recommend taking a look at them.

> - [.vscode/settings.json](.vscode/settings.json) contains configurations for VSCode.
> - [clean/.docker.env](clean/.docker.env) contains environment variables/secrets for your container named `clean`.
> - [solution/.docker.env](solution/.docker.env) contains environment variables/secrets for the `solution` container.

```
cp .vscode/settings.default.json .vscode/settings.json
cp clean/.docker.example.env clean/.docker.env
cp solution/.docker.example.env solution/.docker.env
```

<br>
<br>

<!-- ### 3. Build project

```
docker compose build
``` -->

<!-- <br> -->
<!-- <br> -->

### Step 3: Run project

The workshop is setup with two docker containers I will reference throughout the workshop. One named `clean` and another named `solution`.

- The `clean` container is for the moment completely empty. This is where you will start your django project.
- The `solution` container is fully spec'ed with most of the tools I like to use on my own projects. It serves as an inspiration during your tasks as well as giving you an instant feeling as to what Django can provide.

> The command is expected to display errors for the `clean` container.
> This is because you have not created a project inside it yet.

```
docker compose up
```

The `solution` server is now running on [http://localhost:8002](http://localhost:8002).  
You may browse the admin panel on [http://localhost:8002](http://localhost:8002).
Credentials can be found in [solution/.docker.env](/solution/.docker.env)

<br>
<br>

### Step 4: Install dependencies (optional)

This step is only to enhance the VSCode experience where it can recognise Django, enable formatter, linters etc.

```
cd solution
```

> `pipenv` will recognise dependencies automatically from [Pipfile](/solution/Pipfile).
> `PIPENV_VENV_IN_PROJECT=1` will ensure that the environment is installed within this folder.

```
PIPENV_VENV_IN_PROJECT=1 pyenv exec pipenv install --python 3.11
```

<br>
<br>

### Step 5: Select interpreter in VSCode

`Cmd + Shift + P` --> `Select interpreter` --> `+ Enter interpreter path`

Write `solution/.venv` and hit `Enter`.

<br>
<hr>
<br>

## Documentation

Go to [documentation](/documentation/README.md) to continue with workshop.
