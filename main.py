import random as rand


def get_sequences(file_path: str) -> list:
    genes = []
    current_seq_list = []

    with open(file_path, 'r') as f:
        current_header = next(f).rstrip().upper()
        for raw_line in f:
            # Removing trailing newlines.
            line = raw_line.rstrip().upper()
            if line == '':
                continue
            # Checking if the current line is a header.
            if line[0] == '>':
                # Turning sequence list into one string.
                current_seq = ''.join(current_seq_list)
                genes.append([current_header, current_seq])

                # Setting the current line as the new current
                # header.
                current_header = line
                # Resetting the current sequence list because
                # the previous sequence has ended.
                current_seq_list = []
            else:
                # Adding the current line to the sequence list.
                current_seq_list.append(line)

        # Turning sequence list into one string.
        current_seq = ''.join(current_seq_list)
        genes.append([current_header, current_seq])
        return genes


def shuffler(genes):
    def shuffle_string(seq: str) -> str:
        shuffle_list = list(seq)
        rand.shuffle(shuffle_list)
        return ''.join(shuffle_list)

    with open('output.fasta', 'a+') as f:
        for header, seq in genes:
            f.write(header+'\n')
            f.write(seq + '\n\n')
            for i in range(100):
                f.write(header + ' SHUFFLE' + str(i) + '\n')
                f.write(shuffle_string(seq) + '\n\n')


if __name__ == '__main__':
    file = 'surface_protein_seq.fasta'
    gene_list = get_sequences(file)
    shuffler(gene_list)
