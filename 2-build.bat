@echo off
set filename=%1

echo Building final bin file...
pushd cd
..\tools\mkpsxiso.exe wheel.xml -y -o %filename%_working.iso >> build.log
popd
echo:

echo Build complete!
echo:
pause