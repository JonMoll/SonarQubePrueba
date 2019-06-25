class ClassWithError:
    def __init__(self):
        self.message = 'Hi, Im a class with an error'
        
        return self.message

def HadamardProduct(matrix_a, matrix_b):
    matrix_result = [[0 for col in range(len(matrix_a))] for row in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            matrix_result[i][j] = matrix_a[i][j] * matrix_b[i][j]
    
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