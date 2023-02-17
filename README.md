# django-workshop

<br>
<br>

## Prerequisites

1. `pyenv` (recommended)
2. `python` (3.11)
3. `pipenv`
4. `docker`
5. `docker compose`
6. `vscode` (optional, but recommended)

## Setup

1. Locate directory you want to clone project.

```
git clone git@github.com:emilte/django-workshop.git;
```

<br>

2. Copy environment files.

```
cp .vscode/settings.default.json .vscode/settings.json
cp clean/.docker.example.env clean/.docker.env
cp solution/.docker.example.env solution/.docker.env
```

3. Build project

```
docker compose build
```

3. Run project for initial setup

It's expected to display errors for `clean` container.
This is the container you are about to create a django project inside.
You may stop this afterwards.

```
docker compose up
```

4. Install dependencies

```
cd solution
```

```
PIPENV_VENV_IN_PROJECT=1 pipenv install
```

5. Select interpreter in VSCode

`Cmd + Shift + P` --> `Select interpreter` --> `solution/.venv`

## Documentation

Go to [documentation](/documentation/README.md) to continue with workshop.
