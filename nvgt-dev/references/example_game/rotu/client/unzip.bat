@echo off
title Extracting update, please wait...
timeout /t 2 /nobreak > nul
powershell -Command "Expand-Archive -Path 'rotu.zip' -DestinationPath '.' -Force"
del rotu.zip
title Update completed successfully! Starting game...
timeout /t 1 /nobreak > nul
start rotu.exe
exit
