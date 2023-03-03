/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [Debugger](startproject.md)

# Task: Debugger

This section will instruct you on how to attach a debugger to your container.  
No need to start an entirely new server or environment, just use the already running container 😃

You should probably make a View before doing this in order to have something to debug.

NOTE:

> 1. The docker-compose config and VSCode are already configured to expect a process on port `5678`.
> 2. Because of hot-reload, the debugger process will be restarted with the container when changes are made. You must start re-attach VSCode to continue debugging the "new" code.

<br>
<br>

Table of contents:

- [Step 1: Install debugger](#step-1-install-debugger)
- [Step 2: Initialize debugger](#step-2-initialize-debugger)
- [Step 3: Start VSCode debug session](#step-3-start-vscode-debug-session)
- [Step 4: Set breakpoint](#step-4-set-breakpoint)

<br>
<br>

## Step 1: Install debugger

Install `debugpy` inside the virtual environment of container `clean`.

<details>
<summary>Solution</summary>

From root of project on host machine:

```
docker compose exec clean pipenv run
```

</details>

<br>
<br>

## Step 2: Initialize debugger

Attach a debugger to the django server.
Use host `0.0.0.0` with post `5678`.
Initialize inside the file `clean/root/wsgi.py`.

<details>
<summary>Solution</summary>

See [debugpy.py](/solution/root/debugpy.py) and [wsgi.py](/solution/root/wsgi.py) in solution.

</details>

<br>
<br>

## Step 3: Start VSCode debug session

Go to the debug tab in VSCode in the left sidebar.
At the top you can select which configuration you want to use (see [launch.json](/.vscode/launch.json)).
Select the one for `clean`, the editor should now be orange.

> Ff you have another editor than VSCode, you must configure it yourself. The process is running as mentioned on port `5678`, so in theory anything can listen to it.

<br>
<br>

## Step 4: Set breakpoint

Set a breakpoint 🔴 on a line of code you want to inspect. Preferably inside a View so that you can trigger a request to that endpoint.

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
