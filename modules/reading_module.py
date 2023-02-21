import random


def read_matrix_from_console():
    try:
        N = int(input("Введите количество уравнений в системе: "))
        matrix = []
        for i in range(N):
            row = input()
            row = row.split()
            for j in range(len(row)):
                row[j] = int(row[j])
            matrix.append(row)
        return matrix
    except ValueError:
        return []


def generator():
    matrix = []
    n = random.randint(2, 20)
    for i in range(n):
        row = [random.uniform(-10000000, 10000000) for j in range(n+1)]
        matrix.append(row)
    return matrix


def read_matrix_from_file():
    matrix = []
    with open("modules/matrix.txt", 'r') as file:
        for line in file:
            row = line.split()
            for i in range(len(row)):
                row[i] = float(row[i])
            matrix.append(row)
    return matrix
