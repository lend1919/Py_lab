import numpy as np

def save_result_to_file(result, filename):
    with open(filename, 'w') as file:
        if isinstance(result, np.ndarray):
            for row in result:
                file.write('\t'.join(map(str, row)) + '\n')
        elif isinstance(result, np.generic):
            file.write(str(result))
        else:
            file.write(str(result))

def vector_dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

# Пример векторов и матриц
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

matrix_c = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_d = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Вычисление и сохранение результатов
vector_result = vector_dot_product(vector_a, vector_b)
matrix_result = matrix_multiplication(matrix_c, matrix_d)

save_result_to_file(vector_result, 'vector_result.txt')
save_result_to_file(matrix_result, 'matrix_result.txt')