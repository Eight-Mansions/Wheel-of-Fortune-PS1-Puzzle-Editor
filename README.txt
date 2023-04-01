### Initial Setup ###
1. Open build.bat in a text editor and update the initial lines with name
of your game by updating the following:

set filename=test_project
set working_name=working

2. Open cd/prepare-clean-bin.bat and make the same changes.

3. Drag and drop the bin file of the original game on cd/prepare-clean-bin.bat.
This will extract the bin file into an orig and working folder, create cue files,
and prepare the catalog for rebuilding.


### Building ###
1. Run build.bat to create a new working image in the cd folder.
2. As you add to the game, modify build.bat to copy files into the right place in
the working folder, then those will be picked up by the build.


### Tools ###
1. psximager is used to extract and rebuild the disc image.
2. armsips.exe compiles assembly and inserts them into a psx executable.
3. Atlas.exe is Esper's script insertion tool of choice.
4. DATImageInserter.py is a simple uncompressed image inserter for DAT archives.
Feel free to modify it to your use case.


Ask Aria questions if things don't work or if you have improvements!