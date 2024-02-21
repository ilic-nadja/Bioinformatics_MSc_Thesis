input_file = "/Users/nadja/Downloads/ahl_40.fasta"
output_file = "/Users/nadja/Downloads/filt_dbd40.fasta"

def extract_info(entry):
    # Find the identifier
    identifier_start = entry.find(">") + 1
    identifier_end = entry.find("SV=") + 4
    identifier = entry[identifier_start:identifier_end]

    # Find the characters to retain
    characters_start = entry.find("SV=") + 5
    characters = entry[characters_start:]

    # Adjust the character range to span positions 188-252
    if len(characters) >= 252:
        characters = characters[187:252]
    else:
        characters = characters[187:]

    # Find the next FASTA identifier
    next_identifier_start = characters.find(">")
    if next_identifier_start != -1:
        characters = characters[:next_identifier_start]

    return f">{identifier}\n{characters}\n"

with open(input_file, "r") as file:
    entries = file.read().split(">")[1:]  # Split entries based on ">"

    with open(output_file, "w") as output:
        for entry in entries:
            extracted_entry = extract_info(entry)
            output.write(extracted_entry)
