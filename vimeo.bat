@echo off

set argv1=%1
set argv2=%2

if "%1"=="" (
    if exist venv (
        venv\scripts\activate
        type welcome.txt
    ) else (
        python -m venv venv
        venv\scripts\activate
        pip install -r requirements.txt
        echo Environment configured successfully
    )
) else ( 
    if "%3"==""  (
        python entry.py %argv1% %argv2%
    ) else (
      echo Invalid format or command. Enter [ vimeo --help ] to get help.
    )
)