function slove(matrix) {
    let maxNum = -999999999
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] > maxNum) {
                maxNum = matrix[i][j]
            }
        }
    }
    return maxNum
}

console.log(slove([[20, 50, 10], [8, 33, 145]]))