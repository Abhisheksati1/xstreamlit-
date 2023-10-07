# Debugging

It is possible to run Dotreact apps in dev mode under a debugger.

1. Run Dotreact as a module: `python -m dotreact run --env dev`
2. Set current working directory to the dir containing `dsconfig.py`

## VSCode

The following launch configuration can be used to interactively debug a Dotreact
app with breakpoints.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Dotreact App",
            "type": "python",
            "request": "launch",
            "module": "dotreact",
            "args": "run --env dev",
            "justMyCode": true,
            "cwd": "${fileDirname}/.."
        }
    ]
}
```