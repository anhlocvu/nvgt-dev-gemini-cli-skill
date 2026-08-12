@echo off
setlocal
set "DEST=%USERPROFILE%\.gemini\config\plugins\nvgt-dev-plugin\skills\nvgt-dev"
echo Installing nvgt-dev skill to "%DEST%"
if exist "%DEST%" (
    echo Removing old nvgt-dev installation...
    rmdir /s /q "%DEST%"
)
if not exist "%USERPROFILE%\.gemini\skills" mkdir "%USERPROFILE%\.gemini\skills"
xcopy /E /I /Y "%~dp0nvgt-dev" "%DEST%"
echo.
echo Successfully installed. Restart Antigravity to load the skill.
pause
