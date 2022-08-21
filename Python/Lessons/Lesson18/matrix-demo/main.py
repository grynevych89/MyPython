from matrix import Matrix

if __name__ == '__main__':
    matrixA = Matrix(3, 4, [
        [11, 12, 13, 14],
        [21, 22, 23, 24],
        [31, 32, 33, 34]
    ])
    matrixA.display()

    matrixB = Matrix(3, 4, [
        [41, 42, 43, 44],
        [51, 52, 53, 54],
        [61, 62, 63, 64]
    ])
    matrixB.display()

    matrixC = matrixA + matrixB
    matrixC.display()
