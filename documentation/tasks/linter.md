/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Start project](startproject.md)

# Task: Linter

In this task, you will install and configure a linter to your project. The package to use in this task is `flake8`, a lightweight and fast linter that can cover most of your needs.

The project is already setup with a config file [.flake8](/.flake8).

<br>
<br>

Table of contents:

- [Step 1: Install linter](#step-1-install-linter)
- [Step 2: Setup editor](#step-2-setup-editor)

<br>
<br>

## Step 1: Install linter

1. Install `flake8` inside your virtual environment.
2. Install plugin `flake8-quotes`. Rule to use single quote `'` instead of double quote `"`.
3. Install plugin `flake8-print`. Rule to warn about existing print statements.

<details>
<summary>Solution</summary>

To install (from root of project on host machine):

```
docker compose exec clean pipenv install flake8
```

To run (from root of project on host machine):

```
docker compose exec clean pipenv run flake8 --config .flake8
```

</details>

<br>
<br>

## Step 2: Setup editor

Enable flake8 in VSCode (or other editor).
Point to the config file [.flake8](/.flake8).

> List of rules https://lintlyci.github.io/Flake8Rules/

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
