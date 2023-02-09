[docs](/docs/README.md) / [vscode](vscode.md)

[<- Back to: README](README.md)

# VSCode à la @emilte

<hr>

## Table of contents

- [Table of contents](#table-of-contents)
- [What is this?](#what-is-this)
- [Files explained](#files-explained)
- [Local setup](#local-setup)
  - [Virtual environment](#virtual-environment)
  - [VSCode extensions](#vscode-extensions)
- [Extensions explained](#extensions-explained)
  - [Default](#default)
  - [Recommended](#recommended)

<hr>
<br>
<br>

## What is this?

The current README is designed for development directly inside a running container. This causes issues when the codebase is introduced with lines of code that the running container is unable to compile. You will be stuck in a loop of wanting to fix some code to get the project to compile, whilst being dependent on a working container to develop.

Instead, I propose a local development environment independent from Docker.

> Attaching directly to the container is still useful when you want to utilise the debug server.

<br><br>

## Files explained

Which folders and files are relevant to VScode, what do they mean, and which ones are recognised by VSCode.

- `.vscode/`  
  Folder recognized by VSCode. Contains configurations for workspace.

- `extensions.json`  
  Contains common extensions needed for this project.
  This file is recognised by VSCode, so hopefully it prompts you to install these automatically.

- `extensions.recommended.json`  
  Contains recommended optional extensions for this project.

- `launch.json`  
  Contains configurations for debugging.

- `settings.json`  
  Contains workspace settings for VSCode and extensions. Note that workspace settings takes precedens over user-settings.
  This file is recognised by VSCode and is to be configured to your liking. That's why this file is intentionally excluded from git.

- `settings.default.json`  
  Contains common project-specific settings shared between developers. These settings are project specific and intended to be used ba all team-members. Copy these settings into `settings.json`.

- `settings.suggestions.json`  
  Contains suggestions for useful settings, but not neccessary ones. Copy into `settings.json` if desired.

<br><br>

## Local setup

> Make sure you have downloaded a version of VSCode compatible with your device.  
> MAC: universal or M1.  
> Windows: ...  
> Linux: ...

### Virtual environment

The backend is a Django application, meaning we need to setup a python environment for VSCode.

Command (call inside feide-kp):

```sh
PIPENV_VENV_IN_PROJECT=1 # Ensures folder `.venv` appears in project.
pyenv install # Install python version defined in `.python-version`.
python -m pip install pipenv # Install `pipenv`.
python -m pipenv install -r requirements-frozen.txt # Install dependencies.
python -m pipenv install -r requirements/development.txt # Install dependencies.

```

VSCode should now recognize the environment. If not, you have to manually select interpreter (hint: `CMD+Shift+P`).

<br>

### VSCode extensions

From project folder:

```sh
# Get default settings.
cp .vscode/settings.default.json .vscode/settings.json

```

- Install all extensions from `extensions.json`.
- Install desired extensions from `extensions.recommended.json`.
- Copy desired settings from `settings.suggestions.json` into `settings.json`.

<br><br>

## Extensions explained

This section motivates the multiple extensions relevant for this project.

<br>

### Default

List of extensions you should have in this project. Found in [`extensions.json`](/.vscode/extensions.json).

- `fnando.linter` [link](https://marketplace.visualstudio.com/items?itemName=fnando.linter)  
  idk.

- `ms-python.python` [link](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
  This project uses Django as framework, which is python based. This extension includes neccessary python language support. It also includes `ms-python.vscode-pylance` [(link)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) which is the default language server for VSCode. A language server is able to lint in realtime unlike pylint. It also enables helper/suggestion pallette when developing. `visualstudioexptteam.vscodeintellicode` [(link)](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.vscodeintellicode).

- `orta.vscode-jest` [link](https://marketplace.visualstudio.com/items?itemName=orta.vscode-jest)  
  idk
- `batisteo.vscode-django`
  [link](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)  
  Supports Django syntax in templates (.html) and useful snippets.

- `dbaeumer.vscode-eslint` [link](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)  
  Code quality in frontend.

- `esbenp.prettier-vscode` [link](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)  
  Prettier is a formatting tool for frontend configured in this project (see [`prettierrc.js`](/.prettierrc.js)). This extension

- `editorconfig.editorconfig`
  [link](https://marketplace.visualstudio.com/items?itemName=editorconfig.editorconfig)  
  [EditorConfig](https://editorconfig.org/) configures consistent coding styles across various editors and filetypes.

- `visualstudioexptteam.vscodeintellicode` [link](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.vscodeintellicode)  
  Used in conjunction with `pylance` to enable smart suggestions during development.

<br>

### Recommended

Optional (nice-to-have) extensions for development. They can be found in [`extensions.recommended.json`](/.vscode/extensions.recommended.json).

- `jock.svg` [link](https://marketplace.visualstudio.com/items?itemName=jock.svg)  
   This extension enables language support and preview when writing SVG.

- `albert.tabout` [link](https://marketplace.visualstudio.com/items?itemName=albert.tabout)  
  Tabout makes it easy to "tab out" from brackets `()`, `[]` and `{}`.  
  Example: `return (True|)` -> `return (True)|`

- `mtxr.sqltools` [link](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)  
  SQLTools enables us to connect to a database through VSCode. This extension adds a tab in the sidebar which provides overview of existing tables and columns. It is also able to send queries so we can inspect rows in any given table. Because this project uses PostgreSQL database, the PostgreSQL driver for SQLTools is required, `mtxr.sqltools-driver-pg` ([link](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-pg)). Configuration for connection can be found in [settings.suggestions.json](/.vscode/settings.suggestions.json).

- `eamodio.gitlens` [link](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)  
  Powerful extension to integrate git version control into VSCode. Highly customizable.

- `mikestead.dotenv` [link](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv)  
  Environment-files (.env) have no highlighting by default. This extension fixes that.

- `hediet.vscode-drawio` [link](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)  
  The popular tool [draw.io](draw.io) (now called [diagrams.net](diagrams.net)) enables us to draw diagrams, e.g. ER-diagram for database and modelling tasks.

- `mrorz.language-gettext` [link](https://marketplace.visualstudio.com/items?itemName=mrorz.language-gettext)  
  Django supports localization which generates .po files with translations. This extension provides syntax highlight for these files.

- `gitlab.gitlab-workflow` [link](https://marketplace.visualstudio.com/items?itemName=gitlab.gitlab-workflow)  
  GitLab Workflow integrates the repository directly into VSCode. You will find a 'fox' logo in the sidebar. It's a feature-rich extension. To name a few, it enables autocompletion when editing gitlab config, provides pipeline control, and manages issues and MR's etc.
  Setup can be read on the extension documentation. TL;DR: you need to create a PAT ([Personal Access Token](https://gitlab.sikt.no/-/profile/personal_access_tokens)) on GitLab to give the extension access to repository. A neccessary setting can be found in [settings.suggestions.json](/.vscode/settings.suggestions.json).

- `yzhang.markdown-all-in-one` [link](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)  
  Extension which enables preview while writing markdown (.md). It also has a lot of useful commands, snippets and shortcuts.
  For example enables this extensions auto-generated table of contents used in these docs.

- `ms-azuretools.vscode-docker` [link](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)  
  This project is setup with container-technology with Docker. This extensions integrates Docker functionality.

- `ms-vscode-remote.remote-containers` [link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)  
  Enables VSCode to attach to a running container. Useful for debugging and developing without having to install any dependencies locally.
