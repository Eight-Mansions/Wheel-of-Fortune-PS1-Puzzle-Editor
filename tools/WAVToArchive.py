import subprocess
import os
import sys

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 2:
    print("Usage: <replacement_audio>")
    exit()

replacement_audio = sys.argv[1]

JPSXDEC_COMMAND = "java -jar ..\\tools\\jpsxdec\\jpsxdec.jar -x "# + index_file + " -i "

# Grab the name of the index by grabbing everything before the period
index_name_stripped = replacement_audio.split("[")[0]
index_name = index_name_stripped[0:index_name_stripped.rindex(".")] + ".idx"
index_name = index_name.replace("normalized" + os.sep, "") # This is bad, but go back a folder :P

# Grab the index by reading inside the right-most brackets
# Ex: "C:\Users\yagen\OneDrive\Games\Translations\Galerians\Disc 1\updated_audio\normalized\XA.MXA[0].wav"
index = replacement_audio.split("[")[-1].split("]")[0]
if index == "0.0":
    index = "1"

command = JPSXDEC_COMMAND + "\"" + index_name + "\" -i " + index + " -replaceaudio \"" + replacement_audio + "\""

# Run jpsxdec and insert the wav file
subprocess.run(command)
