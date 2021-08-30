function slove(matrix) {
    let matrix1=matrix.slice().reverse()
    let sumDiag1 = 0
    let sumDiag2 = 0
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (i==j) {
                sumDiag1 += matrix[i][j]
                sumDiag2 += matrix1[i][j]
            }
        }
    }
   
    let result = String(sumDiag1) + ' ' + String(sumDiag2) 
    return result
}

console.log(slove([[3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]]))