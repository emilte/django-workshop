/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Formatter](formatter.md)

# Task: Formatter

> This task requires that you have installed

In this task you will install and configure a formatter named `yapf` for your editor.
`yapf` only cares about whitespace, it will not modify any other characters.

There are several configurations, for example always two empty lines before a class declaration.

> This task is intended to be performed locally on your host machine, not inside docker container.

<br>
<br>

# Step 1: Install yapf

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

## Step 2: Setup editor

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

👈 Back to [Tasks](/documentation/tasks/README.md)
