def process_clstr_file(clstr_file_path, output_tsv_path):
    entries = []
    seq_count = 0

    with open(clstr_file_path, 'r') as clstr_file:
        for line in clstr_file:
            if line.startswith('>Cluster'):
                if entries:
                    entries[-1]['Seq_count'] = seq_count
                cluster_number = int(line.split()[1])
                seq_count = 0
            elif line.strip().endswith(' *'):
                entry = line.strip().split('>', 1)[1].split('...')[0]
                entries.append({'Entry': entry, 'Seq_count': None})
                seq_count += 1
            else:
                seq_count += 1

        if entries:
            entries[-1]['Seq_count'] = seq_count

    with open(output_tsv_path, 'w') as tsv_file:
        tsv_file.write('Entry\tSeq_count\n')
        for entry_info in entries:
            tsv_file.write(f"{entry_info['Entry']}\t{entry_info['Seq_count']}\n")

if __name__ == "__main__":
    clstr_file_path = "/Users/nadja/Downloads/merged_40.clstr"
    output_tsv_path = "output_table.tsv"
    process_clstr_file(clstr_file_path, output_tsv_path)
