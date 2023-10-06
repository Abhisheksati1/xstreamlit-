# Debugging

It is possible to run Dotserve apps in dev mode under a debugger.

1. Run Dotserve as a module: `python -m dotserve run --env dev`
2. Set current working directory to the dir containing `dsconfig.py`

## VSCode

The following launch configuration can be used to interactively debug a Dotserve
app with breakpoints.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Dotserve App",
            "type": "python",
            "request": "launch",
            "module": "dotserve",
            "args": "run --env dev",
            "justMyCode": true,
            "cwd": "${fileDirname}/.."
        }
    ]
}
```