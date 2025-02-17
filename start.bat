@echo off

where python >nul 2>nul if %errorlevel% neq 0 ( echo Python no está instalado. Por favor, instálalo antes de continuar. pause exit /b )

pip install -r requirements.txt

pause

