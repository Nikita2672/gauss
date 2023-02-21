def copy_matrix(matrix):
    matrix_origin = []
    for i in range(len(matrix)):
        mass = []
        for j in range(len(matrix[i])):
            mass.append(float(matrix[i][j]))
        matrix_origin.append(mass)
    return matrix_origin


def count_discrepancy(answers, origin_matrix):
    discrepancy_column = []
    for i in range(len(origin_matrix)):
        left = 0
        for j in range(len(origin_matrix)):
            left += origin_matrix[i][j] * answers[j]
        discrepancy_column.append(origin_matrix[i][-1] - left)
    return discrepancy_column

