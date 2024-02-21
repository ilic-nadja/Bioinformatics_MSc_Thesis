# Path to the input FASTA file
fasta_file="/Users/nadja/Desktop/Semester III- Thesis/analysis attempts/vol.2 - uniprot data/buncha 19:06 merge fasta and entreis shiz/ahl_sbd_new.fasta"
# Path to the text file containing the identifiers
entry_file="/Users/nadja/Desktop/Semester III- Thesis/analysis attempts/vol.2 - uniprot data/buncha 19:06 merge fasta and entreis shiz/entry_ahl.txt"
# Path to the output FASTA file
output_file="/Users/nadja/Downloads/output.fasta"

def extract_sequences(fasta_file, entry_file, output_file):
    entry_set = set()
    with open(entry_file, 'r') as entry:
        for line in entry:
            entry_set.add(line.strip())

    with open(fasta_file, 'r') as fasta, open(output_file, 'w') as output:
        write_line = False
        for line in fasta:
            if line.startswith('>'):
                header = line.split('|')[1].split('|')[0]
                if header in entry_set:
                    write_line = True
                    output.write(line)
                else:
                    write_line = False
            elif write_line:
                output.write(line)

extract_sequences(fasta_file, entry_file, output_file)
