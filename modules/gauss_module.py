def diagonal_matrix(matrix):
    is_valid = True
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            for j in range(i + 1, len(matrix)):
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix)+1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
        else:
            is_valid = False
            break
    if is_valid:
        return matrix
    else:
        return []


def solving_equations(matrix):
    answer = []
    for i in range(len(matrix) - 1, -1, -1):
        k = matrix[i][i]
        right = matrix[i][len(matrix)]
        left = 0
        index = 0
        for j in range(len(matrix) - 1, i, -1):
            left += (matrix[i][j] * answer[index])
            index += 1
        solution = (right - left) / k
        answer.append(solution)
    return answer


def gauss_method(matrix):
    if not is_matrix_valid(matrix):
        return {}
    matrix = diagonal_matrix(matrix)
    if len(matrix) == 0:
        return {}
    answer = solving_equations(matrix)
    det = str(determinant(matrix))
    answer = answer[::-1]
    return {"matrix": matrix, "det": det, "answer": answer}


def determinant(matrix):
    det = 1
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det


def is_matrix_valid(matrix):
    try:
        rows = len(matrix)
        for i in range(1, rows):
            if len(matrix[i]) != len(matrix[i-1]):
                return False
            if matrix[i][i] == 0:
                return False
        if matrix[0][0] == 0:
            return False
        return True
    except IndexError:
        return False


def show_result(result):
    if len(result) == 0:
        print("Matrix is not valid")
    else:
        print("-" * 1000)
        print("det:= ", result["det"])
        print("-" * 1000)
        print("Diagonal matrix:")
        for i in range(len(result["matrix"])):
            print(result["matrix"][i])
        print("-" * 1000)
        print("Solution:")
        for i in range(len(result["answer"])):
            print(f"x{i}:= " + str(result["answer"][i]))
        print("-" * 1000)
