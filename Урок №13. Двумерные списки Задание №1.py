import random
def gen_matrix(line, col, min=-100, max=100):
    return [[random.randint(min, max) for j in range(col)] for i in range(line)]

def add_matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1) != len(matrix2):
        raise ValueError
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]

random_line = random.randint(1, 10)
random_col = random.randint(1, 10)
matrix_1 = gen_matrix(random_line, random_col)
matrix_2 = gen_matrix(random_line, random_col)

matrix_3 = add_matrix(matrix_1, matrix_2)
print(matrix_3)




