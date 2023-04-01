@echo off
set filename=%1
set puzzle_file=%2
set working_name=%3

echo Wheel of Fortune (PS1) - Custom Clue Creation
echo #############################################
echo:

echo Clearing out the old files and creating a clean workspace...
rmdir /s /q cd\%working_name% 1>nul
Xcopy /E /q cd\orig\ cd\%working_name%\ 1>nul
echo:

echo Compiling clues into a game binary...
python tools\WheelOfFortuneClueWriter.py puzzles\%puzzle_file% cd\working\PUZZLES.BIN
echo:
