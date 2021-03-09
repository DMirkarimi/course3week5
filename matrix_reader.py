import numpy as np
import matplotlib.pyplot as plt


def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if line:
                if line[0] != '#':
                    temp_list = []
                    for value in line.split(' ')[2:]:
                        if value:
                            temp_list.append(value)
                    matrix.append(temp_list)

    return np.array(matrix, dtype='float')


if __name__ == '__main__':
    matrix = read_matrix('matrix_real.pim')
    inds = np.tril_indices(len(matrix), -1)
    percs = matrix[inds]
    plt.hist(percs, bins=50, lw=1)
    # plt.yscale('log')
    # plt.xticks(np.arange(0, 100, 1.0))
    plt.show()
