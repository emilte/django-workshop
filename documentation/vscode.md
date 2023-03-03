/ [Documentation](/documentation/README.md) / [vscode](vscode.md)

# VSCode explained

This is not a task, just extra context information about the VSCode configurations.

<hr>

## Table of contents

- [Table of contents](#table-of-contents)
- [Files explained](#files-explained)
- [Extensions explained](#extensions-explained)
  - [Default](#default)

<hr>
<br>
<br>

## Files explained

Which folders and files are relevant to VScode, what do they mean, and which ones are recognised by VSCode.

- `.vscode/`  
  Folder recognized by VSCode. Contains configurations for workspace.

- `extensions.json`  
  Contains common extensions needed for this project.
  This file is recognised by VSCode, so hopefully it prompts you to install these automatically.

- `launch.json`  
  Contains configurations for debugging.

- `settings.default.json`  
  Contains common project-specific settings. Not recognised by VSCode, so these settings must be copied into `settings.json` to take effect.

- `settings.json`  
  Contains workspace settings for VSCode and extensions. Note that workspace settings take precedens over user settings.
  This file is recognised by VSCode and is to be configured to your liking. For this reason, the file is intentionally excluded from version control.

<br><br>

## Extensions explained

This section motivates the multiple extensions relevant for this project.

<br>

### Default

List of extensions you should have in this project. Found in [`extensions.json`](/.vscode/extensions.json).

- `ms-python.python` [link](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
  This project uses Django as framework, which is python based. This extension includes neccessary python language support. It also includes `ms-python.vscode-pylance` [(link)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) which is the default language server for VSCode. A language server is able to lint in realtime unlike pylint. It also enables helper/suggestion pallette when developing. `visualstudioexptteam.vscodeintellicode` [(link)](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.vscodeintellicode).

- `batisteo.vscode-django`
  [link](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)  
  Supports Django syntax in templates (.html) and useful snippets.

- `editorconfig.editorconfig`
  [link](https://marketplace.visualstudio.com/items?itemName=editorconfig.editorconfig)  
  [EditorConfig](https://editorconfig.org/) configures consistent coding styles across various editors and filetypes.

- `visualstudioexptteam.vscodeintellicode` [link](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.vscodeintellicode)  
  Used in conjunction with `pylance` to enable smart suggestions during development.
