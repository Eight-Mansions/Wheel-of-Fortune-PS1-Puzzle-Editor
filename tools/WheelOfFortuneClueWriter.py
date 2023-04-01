import sys


def format_clue(clue):
    # Each clue is on 4 rows of 12, 14, 14, 12. For simplicity, let's think of it as 12
    formatted_clues = ["", "", "", ""]
    index = 0
    result_hex = ""

    # The game expects all letters to be uppercase
    clue = clue.upper()

    for word in clue.split(" "):
        if len(formatted_clues[index]) + len(word) > 12:
            index += 1
        if index > 3:
            print(f"Error: phrase too long! {clue}")
            return
        formatted_clues[index] += word + " "

    # If we don't use all 4 lines, shift down to avoid the first
    if index < 3:
        formatted_clues[3] = formatted_clues[2]
        formatted_clues[2] = formatted_clues[1]
        formatted_clues[1] = formatted_clues[0]
        formatted_clues[0] = ""

    # Add a little padding
    for index, formatted_clue in enumerate(formatted_clues):
        if len(formatted_clue) <= 10 or (len(formatted_clue) <= 12 and (index == 1 or index == 2)):
            formatted_clues[index] = " " + formatted_clues[index]

    # Determine the hex
    for index, formatted_clue in enumerate(formatted_clues):
        if 0 < index < 3:
            max_range = 14
        else:
            max_range = 12
        for x in range(0, max_range):
            if x >= len(formatted_clue):
                result_hex += "00"
            elif formatted_clue[x] == " ":
                result_hex += "00"
            else:
                result_hex += formatted_clue[x].encode("utf-8").hex()

    return result_hex


# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 2:
    print("Usage: <input_clue_file> <output_bin_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

clues = {}
clue_count = 0

category_ids = {"people": "02",
                "title": "03",
                "place": "05",
                "thing": "06",
                "quotation": "07",
                "event": "08",
                "fictional character": "09",
                "occupation": "0E",
                "foreign word": "14",
                "gods": "15",
                "title/author": "16",
                "slang": "17",
                "nickname": "19",
                "fictional characters": "1B",
                "creatures": "22",
                "things": "25",
                "who said it?": "28"}

with open(input_file, "r") as file:

    current_category = ""
    for line in file.readlines():

        # Remove any lingering whitespace
        line = line.strip()

        # Ignore comments or blank lines
        if line == "" or line.startswith("#"):
            continue

        # If this is a section header, grab the category name
        if line.startswith("="):
            current_category = line.replace("=", "").strip().lower()

            if "(" in current_category:
                current_category = current_category.split("(")[0].strip()

            # On the off chance there's a repeat category, append to that one
            if current_category not in clues:
                clues[current_category] = []
            continue

        # All other lines are clues
        clues[current_category].append(line.replace("\\\\", "").strip())
        clue_count += 1


with open(output_file, "wb") as hex:
    # Write the initial header
    hex.write(int.to_bytes(clue_count, 2, byteorder="big"))
    hex.write(bytes.fromhex("AF682F6C207265636F726473202B7265636C656E2B33372B3220425954455300000000000000"))

    for category in clues:
        for clue in clues[category]:
            # Separate any clue/answer prompts
            clue_split = clue.split("|", 1)

            # Write the clue header
            hex.write(bytes.fromhex("0D0A"))

            formatted_clue_hex = format_clue(clue_split[0])

            if not formatted_clue_hex:
                continue

            # Write out the clue
            hex.write(bytes.fromhex(formatted_clue_hex))

            # Write the clue type(?)
            hex.write(bytes.fromhex(category_ids[category]))

            # Write out the extended clue
            if len(clue_split) > 1:
                hex.write(clue_split[1].upper().encode("utf-8"))

                for _ in range(1, 121 - len(clue_split[1])):
                    hex.write(bytes.fromhex("00"))

            # If there's no extended clue, write out 00s
            else:
                for _ in range(1, 121):
                    hex.write(bytes.fromhex("00"))

    # Write out one final 0D0A because the Elder Gods demand it
    hex.write(bytes.fromhex("0D0A"))

    print("Complete!")
    print(f"Found total of {clue_count} clues.")
