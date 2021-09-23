function solve(matrix) {

    let matrix1 = []
    for (let i = 0; i < matrix.length; i++) {
        matrix1.push(matrix[i].split(' '))
    }

    let matrixReverse = matrix1.slice().reverse()
    let sumDiag1 = 0
    let sumDiag2 = 0
    for (let i = 0; i < matrix1.length; i++) {
        for (let j = 0; j < matrix1.length; j++) {
            if (i == j) {
                sumDiag1 += Number(matrix1[i][j])
                sumDiag2 += Number(matrixReverse[i][j])
            }
        }
    }
    if (sumDiag1 == sumDiag2) {
        for (let i = 0; i < matrix1.length; i++) {
            for (let j = 0; j < matrix1.length; j++) {
                if (i != j && matrix1.length - 1 - i != j) {
                    matrix1[i][j] = sumDiag1
                }
            }
        }
    }

    for (let i = 0; i < matrix1.length; i++) {
        console.log(matrix1[i].join(' '))
    }
}

solve(['5 3 12 3 1',
    '11 4 23 2 5',
    '101 12 3 21 10',
    '1 4 5 2 2',
    '5 22 33 11 1']
)