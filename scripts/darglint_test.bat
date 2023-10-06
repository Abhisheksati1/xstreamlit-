@echo off
cd ..

echo "start darglint"

echo "dotserve folder"
for /R dotserve %%f in (*.py) do (
    echo %%f
    echo %%f|findstr /r "^.*dotserve\\ds\.py$"
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
