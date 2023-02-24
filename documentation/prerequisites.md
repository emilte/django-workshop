# Prerequisites

1. `pyenv` (recommended)
2. `python` (3.11)
3. `pipenv` (sub-package of python)
4. `docker`
5. `docker compose`
6. `vscode` (optional, but recommended)

<br>
<br>

# 1. Install pyenv

MacOS:

```
brew install pyenv
```

Windows:
https://github.com/pyenv-win/pyenv-win

<br>
<br>

## 2. Install python

> `pyenv` will automatically recognise the file I made [.python-version](/.python-version).
> It will therefore use this version when you are inside the workspace of this workshop.

This will install python 3.11:

```
pyenv install
```

You may now execute commands with this python version via `pyenv exec`:

```
pyenv exec python -V
```

<br>
<br>

## 3. Install pipenv

`pipenv` is a sub-package of python that can be install via `pip`.  
`-m` calls upon a sub-module.

```
pyenv exec python -m pip install pipenv
```

You can now use `pipenv`. Example:

```
pyenv exec python -m pipenv
```

<br>
<br>

## 4. Docker

https://docs.docker.com/get-docker/

<br>
<br>

## 5. docker compose

https://docs.docker.com/compose/install/

<br>
<br>

## 6. VSCode

https://code.visualstudio.com/download
