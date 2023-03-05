/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Formatter](formatter.md)

# Task: Formatter

In this task you will install and configure a formatter named `yapf` for your editor.
`yapf` only cares about whitespace, it will not modify any other characters.

You already have this setup configured in the root directory of this project (given that you completed the local setup in README). For this task, you can open a new window in VSCode from the folder `clean`. That way, you will start without any interpreter or vscode settings.

Yapf have several configurations, for example always two empty lines before a class declaration.

> This task is intended to be performed locally on your host machine, not inside docker container.
> The local setup from README is _required_ for this task.

<br>
<br>

Table of contents:

- [Step 1: Install yapf](#step-1-install-yapf)
- [Step 2: Setup editor](#step-2-setup-editor)

<br>
<br>

## Step 1: Install yapf

Install `yapf` through `pipenv` from root of project on host machine.

<details>
<summary>Solution</summary>

From root of project on host machine:

```
pyenv exec pipenv install yapf
```

</details>

<br>
<br>

## Step 2: Select interpreter

Open a new window in VSCode from the folder `clean` and select the `.venv` folder as interpreter.

See [README](/README.md#step-4-install-dependencies-optional) step 4 and 5 for these instruction.

<br>
<br>

## Step 3: Setup editor

Tell VSCode to format file on save with `yapf`.

<details>
<summary>Solution</summary>

Add this to file [/.vscode/settings.json](/.vscode/settings.json):

```json
{
    ...
    // Formatting:
    "python.formatting.provider": "yapf",
    "editor.formatOnSave": true,
}
```

</details>

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
