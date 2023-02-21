import time
from modules import gauss_module, reading_module, util

print("""
    1: generate random
    2: read from file
    3: read from console
""")
matrix = [[]]
while True:
    a = input("Введите число (1-3): ")
    if a == str(1):
        matrix = reading_module.generator()
        break
    elif a == str(2):
        matrix = reading_module.read_matrix_from_file()
        break
    elif a == str(3):
        matrix = reading_module.read_matrix_from_console()
        break


matrix_origin = util.copy_matrix(matrix)
start_time = time.perf_counter_ns()
result = gauss_module.gauss_method(matrix)
elapsed_time = time.perf_counter_ns() - start_time
gauss_module.show_result(result)
print(f"Elapsed time: {elapsed_time} nanoseconds")
print("-" * 1000)
print("discrepancy:", util.count_discrepancy(result["answer"], matrix_origin))
