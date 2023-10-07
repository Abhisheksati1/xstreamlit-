@echo off
cd ..

echo "start darglint"

echo "dotreact folder"
for /R dotreact %%f in (*.py) do (
    echo %%f
    echo %%f|findstr /r "^.*dotreact\\ds\.py$"
    if errorlevel 1 (
        poetry run darglint %%f
    )
)

echo "tests folder"
for /R tests %%f in (*.py) do (
    echo %%f
    poetry run darglint %%f
)

echo "darglint finished"
pause
