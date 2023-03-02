/ [Menu](/documentation/README.md) / [Prerequisites](prerequisites.md)

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

`pyenv` is a python version manager.  
It provides easy installation and usage of multiple versions of python.

<details>
<summary>Simplified overview of what pyenv can achieve</summary>

![Pyenv overview](/documentation/images/pyenv.png)

</details>

<br>

MacOS:

```
brew install pyenv
```

Windows:
https://github.com/pyenv-win/pyenv-win

<br>
<br>

## 2. Install python

> If you don't want `pyenv`, install python 3.11 manually.

```
pyenv install 3.11.0
```

You may now execute commands with this python version via `pyenv exec`:

> `pyenv` will automatically recognise the file I made [.python-version](/.python-version).  
> It will attempt use this version when you are inside the directory of this workshop.

```
pyenv exec python -V
```

<br>
<br>

## 3. Install pipenv

`pipenv` is a sub-package of python that can be install via `pip`.  
`-m` calls upon a sub-module.

> This is the python equivalent of `npm`/`yarn`.  
> Installing packages via `pipenv` will download them into folder `.venv/`, similar to `node_modules/`.

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
