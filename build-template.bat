@echo off
set filename=wheel_of_fortune
set puzzle_file=Clues.txt

echo Template build starting...
echo:

call 1-prepare.bat %filename% %puzzle_file%

:: Add custom asset insertion here

call 2-build.bat %filename%
