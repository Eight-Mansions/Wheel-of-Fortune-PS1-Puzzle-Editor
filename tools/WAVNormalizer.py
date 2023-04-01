import sys
from pathlib import Path
from pydub import AudioSegment
import os

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 4:
    print("Usage: <new_audio_folder> <old_audio_folder> <output_folder>")
    exit()

new_audio_folder = sys.argv[1]
old_audio_folder = sys.argv[2]
output_folder = sys.argv[3]


def read_directory(directory):
    """
    Scans the given directory recursively and parses any files within
    :param directory: Current directory to scan
    """
    for path in Path(directory).glob("*.wav"):
        if path.is_file():
            normalize_wav(path)


def normalize_wav(new_wav_path):
    """
    Compares the given wav file with the original version, then pads silence until
    they're the same size
    :param new_wav_path:
    :return:
    """
    new_audio = AudioSegment.from_wav(str(new_wav_path))

    old_wav_filepath = os.path.join(old_audio_folder, new_wav_path.name)
    old_audio = AudioSegment.from_wav(old_wav_filepath)

    difference = len(old_audio) - len(new_audio)
    # If the old audio is longer, then pad it
    if difference > 0:
        print("Needs " + str(difference) + "ms of padding: " + str(new_wav_path))
        silence = AudioSegment.silent(duration=difference)
        new_audio = new_audio + silence
    elif difference < 0:
        print("WARNING! " + str(new_wav_path) + " was longer than the original! File will be truncated!")
        new_audio = new_audio[0:len(old_audio)]
    else:
        print("Already the right size: " + str(new_wav_path))

    new_audio = normalize_bytes(new_audio, old_audio)
    new_audio.export(os.path.join(output_folder, new_wav_path.name), format="wav")


def normalize_bytes(new_audio, old_audio):
    # Additional byte adjustments since the millisecond count isn't byte accurate
    new_frame_count = new_audio.frame_count()
    old_frame_count = old_audio.frame_count()
    frame_count_difference = int(new_frame_count - old_frame_count)

    # If new audio is too long, chop off some bytes from the end
    if frame_count_difference > 0:
        new_audio._data = new_audio._data[0:len(new_audio._data) - (4 * frame_count_difference)]

    # Otherwise if it's too short, append some null bytes
    else:
        new_audio._data += bytes(abs(frame_count_difference * 4))

    # Verify that they're now equal
    assert new_audio.frame_count() == old_frame_count
    return new_audio


read_directory(new_audio_folder)
print("Normalization complete!")
