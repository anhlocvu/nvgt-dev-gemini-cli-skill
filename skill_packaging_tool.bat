@echo off
cd nvgt-dev
tar -a -c -f ../nvgt-dev.zip *
cd ..
ren nvgt-dev.zip nvgt-dev.skill
echo Successfully packaged
pause