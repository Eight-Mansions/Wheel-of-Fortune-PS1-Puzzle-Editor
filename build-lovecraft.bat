@echo off
set filename=lovecraft_wheel_of_fortune
set puzzle_file=Lovecraftian_Clues.txt
set working_name=working

echo Lovecraft build starting...
echo:

call 1-prepare.bat %filename% %puzzle_file% %working_name%

:: Add custom asset insertion here
echo Copying over TIM edits...
Xcopy /E /q /Y tims\ cd\%working_name%\
echo:

:: TODO: Debug the audio insertion later
::echo Copying over XA edits...
::python tools\WAVNormalizer.py updated_audio updated_audio\original updated_audio\normalized
::for %%i in (updated_audio\normalized\*) do (python ..\tools\WAVToArchive.py %%i)
::echo:

call 2-build.bat %filename%
