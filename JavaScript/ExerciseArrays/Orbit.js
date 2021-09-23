function solve(input) {
    let [n, m, x, y] = input
    let matrix = []
    for (let i = 0; i < n; i++) {
        matrix.push([])
        for (let j = 0; j < m; j++) {  
            matrix[i].push(0)
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            let a = Math.abs(i - x) >= Math.abs(j - y) ? Math.abs(i - x) : Math.abs(j - y)
            matrix[i][j] = a + 1
        }
    }
    for (let i = 0; i < n; i++) {
        console.log(matrix[i].join(' '))
    }
}

solve([4, 4, 0, 0])