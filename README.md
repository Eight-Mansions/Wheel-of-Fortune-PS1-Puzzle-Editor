# Wheel-of-Fortune-Puzzle-Editor
### Initial Setup ###
1. Use `isodump.exe` in the `tools` folder to extract your copy of the game to `cd\orig`.
2. Place a copy of the original bin file named `Wheel_of_Fortune_USA.bin` in the `cd` folder.

TODO: Add a script to handle this


### Custom Clues ###
Under the `puzzles` folder, check out `Clues_Template.txt` for a list of categories. Add any clue you wish under any category, then save as your own file. View the instructions at the top of the template for more details.

### Building ###
1. Run `build-lovecraft.bat` to create a new working Lovecraftian image in the cd folder. Otherwise, modify `build-template.bat` to use your own clue file.
2. If you add any asset modifications (custom images, video), update your build script like how `build-lovecraft.bat` adds in custom images.


Ask Aria questions if things don't work or if you have improvements!