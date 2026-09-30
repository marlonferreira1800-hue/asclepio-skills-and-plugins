@echo off
cd /d "%~dp0"
python "skills\medir-tokens\scripts\tokenmeter.py" dashboard --out "painel.html"
if errorlevel 1 (pause & exit /b 1)
start "" "%~dp0painel.html"
