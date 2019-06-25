def HadamardProduct(matrix_a, matrix_b):
    matrix_result = matrix_a

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b)):
            matrix_result[i][j] = matrix_a[i][j] * matrix_a[i][j]
    
    return matrix_result

def main():
    matrix_a = [[2, 2, 2],
                [2, 2, 2],
                [2, 2, 2]]
    
    matrix_b = [[3, 3, 3],
                [3, 3, 3],
                [3, 3, 3]]
    
    matrix_c = [[4, 4],
                [4, 4]]

    hadamard = HadamardProduct(matrix_a, matrix_b)
    
    print('The Hadamard Product of')
    print(matrix_a)
    print('and')
    print(matrix_b)
    print('is')
    print(hadamard)

if __name__ == '__main__':
    main()