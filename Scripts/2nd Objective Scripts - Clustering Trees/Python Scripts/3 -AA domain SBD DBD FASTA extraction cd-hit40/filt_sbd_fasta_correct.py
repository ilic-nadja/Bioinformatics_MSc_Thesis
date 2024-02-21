input_file = "/Users/nadja/Downloads/ahl_40.fasta"
output_file = "/Users/nadja/Downloads/filt_sbd40.fasta"

def extract_info(entry):
    # Find the identifier
    identifier_start = entry.find(">") + 1
    identifier_end = entry.find("SV=") + 4
    identifier = entry[identifier_start:identifier_end]

    # Find the characters to retain
    characters_start = entry.find("SV=") + 5
    characters_end = characters_start + 180  # Modify this line - captures kinda random len cuz wanna cut off 26-162 anyways
    characters = entry[characters_start:characters_end]

    # Adjust the character range to span positions 26-162
    characters = characters[25:163]

    return f">{identifier}\n{characters}\n"

with open(input_file, "r") as file:
    entries = file.read().split(">")[1:]  # Split entries based on ">"

    with open(output_file, "w") as output:
        for entry in entries:
            extracted_entry = extract_info(entry)
            output.write(extracted_entry)
