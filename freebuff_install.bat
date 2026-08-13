@echo off
setlocal

set "DEST_FREEBUFF=%USERPROFILE%\.freebuff\skills\nvgt-dev"
set "DEST_CODEBUFF=%USERPROFILE%\.codebuff\skills\nvgt-dev"

echo Installing nvgt-dev skill to Freebuff...
if exist "%DEST_FREEBUFF%" (
    echo Removing old Freebuff nvgt-dev installation...
    rmdir /s /q "%DEST_FREEBUFF%"
)
if not exist "%USERPROFILE%\.freebuff\skills" mkdir "%USERPROFILE%\.freebuff\skills"
xcopy /E /I /Y "%~dp0nvgt-dev" "%DEST_FREEBUFF%"

echo.
echo Installing nvgt-dev skill to Codebuff...
if exist "%DEST_CODEBUFF%" (
    echo Removing old Codebuff nvgt-dev installation...
    rmdir /s /q "%DEST_CODEBUFF%"
)
if not exist "%USERPROFILE%\.codebuff\skills" mkdir "%USERPROFILE%\.codebuff\skills"
xcopy /E /I /Y "%~dp0nvgt-dev" "%DEST_CODEBUFF%"

echo.
echo Successfully installed. Restart Freebuff/Codebuff to load the skill.
pause
