/ [Menu](/documentation/README.md) / [Useful commands](useful-commands.md)

# Useful commands

Here you can find a list of useful commands for the workshop.  
To avoid confusion of which context to run each command, I strive to make them all usable
from the host-machine.

This is the general architecture of the repository.  
It becomes significantly easier to remember the long chain of commands when you realise what each segment does.  
(Replace `clean` with `solution` to enter the other container)

Example to list all files inside the container:

```
docker compose exec clean ls -la
```

![Chain of commands](/documentation/images/commands.png)

<br>
<br>

Table of contents:

- [🐳 Docker](#-docker)
  - [🐳 Docker: Open shell in container](#-docker-open-shell-in-container)
  - [🐳 Docker: Run command inside already running container](#-docker-run-command-inside-already-running-container)
  - [🐳 Docker: Build project](#-docker-build-project)
  - [🐳 Docker: Start all containers](#-docker-start-all-containers)
  - [🐳 Docker: Start individual container](#-docker-start-individual-container)
  - [🐳 Docker: Run a one-off command with new container](#-docker-run-a-one-off-command-with-new-container)
  - [🐳 Docker: Remove containers](#-docker-remove-containers)
- [🐍 Python](#-python)
  - [🐍 Pyenv: Install python](#-pyenv-install-python)
  - [🐍 Python: Call submodule of Python](#-python-call-submodule-of-python)
  - [🐍 Python: Install pipenv](#-python-install-pipenv)
  - [🐍 Pipenv: Install virtual environment with dependencies](#-pipenv-install-virtual-environment-with-dependencies)
  - [🐍 Pipenv: Install package](#-pipenv-install-package)
  - [🐍 Pipenv: Uninstall package](#-pipenv-uninstall-package)
  - [🐍 Pipenv: Run command inside virtual environment](#-pipenv-run-command-inside-virtual-environment)
  - [🐍 Django: Show all commands](#-django-show-all-commands)
  - [🐍 Django: Run command](#-django-run-command)
  - [🐍 Django: Makemigrations](#-django-makemigrations)
  - [🐍 Django: Migrate](#-django-migrate)
  - [🐍 Django: Open shell](#-django-open-shell)

<br>
<hr>
<br>

## 🐳 Docker

<br>
<br>

### 🐳 Docker: Open shell in container

> `<container-name>` is defined under `services` in [docker-compose.yml](/docker-compose.yml).

```bash
docker compose exec <container-name> <command>
```

```bash
# Example:
docker compose exec clean bash
```

<br>
<br>

### 🐳 Docker: Run command inside already running container

> `<container-name>` is defined under `services` in [docker-compose.yml](/docker-compose.yml).

```bash
docker compose exec <container-name> <command>
```

```bash
# Example:
docker compose exec clean echo "Hello World!"
```

<br>
<br>

### 🐳 Docker: Build project

```bash
docker compose build
```

<br>
<br>

### 🐳 Docker: Start all containers

```bash
docker compose up
```

<br>
<br>

### 🐳 Docker: Start individual container

> `<container-name>` is defined under `services` in [docker-compose.yml](/docker-compose.yml).

```bash
docker compose up <container-name>
```

```bash
# Example:
docker compose up clean
```

<br>
<br>

### 🐳 Docker: Run a one-off command with new container

> `--rm` removes container after exiting.  
> `<container-name>` is defined under `services` in [docker-compose.yml](/docker-compose.yml).

```bash
docker compose run --rm <container-name> <command>
```

```bash
# Example:
docker compose run --rm clean echo "Hello World!"
```

<br>
<br>

### 🐳 Docker: Remove containers

> `<container-name>` is defined under `services` in [docker-compose.yml](/docker-compose.yml).

```bash
docker compose down
```

<br>
<hr>
<br>

## 🐍 Python

<br>

### 🐍 Pyenv: Install python

> `pyenv` must be installed.  
> Must run inside same directory as [.python-version](/.python-version) to recognise version automatically. Otherwise specify manually.

```bash
pyenv install
```

```bash
# Explicitly
pyenv install --python 3.11
```

<br>
<br>

### 🐍 Python: Call submodule of Python

```bash
python -m <module>
```

```bash
# Example:
python -m pip
```

<br>
<br>

### 🐍 Python: Install pipenv

Pipenv is a packet manager with virtual environment.

> Python equivalent of `npm`/`yarn`.

```bash
python -m pip install pipenv
```

<br>
<br>

### 🐍 Pipenv: Install virtual environment with dependencies

> Must run inside same directory as [Pipfile](/solution/Pipfile) to recognise dependencies. Similar to `package.json`.

> `PIPENV_VENV_IN_PROJECT=1` creates the folder `.venv` inside the same directory.

```bash
PIPENV_VENV_IN_PROJECT=1 python -m pipenv install
```

<br>
<br>

### 🐍 Pipenv: Install package

```bash
python -m pipenv install <package>
```

```bash
# Inside container:
docker compose exec clean python -m pipenv install <package>
```

<br>
<br>

### 🐍 Pipenv: Uninstall package

```bash
python -m pipenv uninstall <package>
```

```bash
# Inside container:
docker compose exec clean python -m pipenv uninstall <package>
```

<br>
<br>

### 🐍 Pipenv: Run command inside virtual environment

```bash
python -m pipenv run <command>
```

```bash
# Example:
python -m pipenv run python -V
```

```bash
# Inside container:
docker compose exec clean python -m pipenv run python -V
```

<br>
<br>

### 🐍 Django: Show all commands

```bash
python -m pipenv run python manage.py
```

```bash
# Inside container:
docker compose exec clean python -m pipenv run python manage.py
```

<br>
<br>

### 🐍 Django: Run command

```bash
# Locally:
python -m pipenv run python manage.py <command>
```

```bash
# Inside container:
docker compose exec clean python -m pipenv run python manage.py <command>
```

<br>
<br>

### 🐍 Django: Makemigrations

Scans all files named `models.py` and creates migrations for the database.

> NOTE: Does not apply migrations.

```bash
# Locally:
python -m pipenv run python manage.py makemigrations
```

```bash
# Inside container:
docker compose exec clean python -m pipenv run python manage.py makemigrations
```

<br>
<br>

### 🐍 Django: Migrate

Applies all migrations to the database.

```bash
# Locally:
python -m pipenv run python manage.py migrate
```

```bash
# Inside container:
docker compose exec clean python -m pipenv run python manage.py migrate
```

<br>
<br>

### 🐍 Django: Open shell

Python shell with access to all dependencies and database.

```bash
python -m pipenv run python manage.py shell
```

```bash
# Inside container:
docker compose exec clean python -m pipenv run python manage.py migrate
```

<br>

[👆 Back to top](#useful-commands)

[👈 Back to Tasks](/documentation/tasks/README.md)
