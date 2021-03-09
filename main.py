def get_sequences(file_path: str) -> dict:
    genes = {}
    current_seq_list = []

    with open(file_path, 'r') as f:
        current_header = next(f)
        for raw_line in f:
            # Removing trailing newlines.
            line = raw_line.rstrip().upper()
            if line == '':
                continue
            # Checking if the current line is a header.
            if line[0] == '>':
                # Turning sequence list into one string.
                current_seq = ''.join(current_seq_list)
                genes[current_header] = current_seq

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
        genes[current_header] = current_seq
        return genes
