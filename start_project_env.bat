
@echo off
cd /d %~dp0
python -m venv venv
call venv\Scripts\activate.bat
echo Виртуальное окружение создано и активировано.
cmd /k
