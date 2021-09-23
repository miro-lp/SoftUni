function solve(input) {
    let matrix = [[false, false, false],
    [false, false, false],
    [false, false, false]]
    let player1 = 'X'
    let player2 = 'O'
    function printBoard(matrix){
        for (let i =0; i<matrix.length;i++){
            console.log(matrix[i].join('\t'))
        }
    }
    isWin =false

    for (i = 0; i < input.length; i++) {
        
        let coord = input[i].split(' ')
        if (matrix[Number(coord[0])][Number(coord[1])] != false) {
            console.log("This place is already taken. Please choose another!")
            continue
        }
        matrix[Number(coord[0])][Number(coord[1])] = player1
        let player11 =  player1
        let player22 = player2
        player1 = player22
        player2 = player11

        if (matrix[0][0] ==matrix[0][1] && matrix[0][1] ==matrix[0][2] && matrix[0][1] != false){
            console.log( `Player ${matrix[0][0] } wins!` )
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[1][0] ==matrix[1][1] && matrix[1][1] ==matrix[1][2] && matrix[1][1] != false){
            console.log( `Player ${matrix[1][0] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[2][0] ==matrix[2][1] && matrix[2][1] ==matrix[2][2] && matrix[2][1] != false){
            console.log( `Player ${matrix[2][0] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[0][0] ==matrix[1][1] && matrix[1][1] ==matrix[2][2] && matrix[0][0] != false){
            console.log( `Player ${matrix[0][0] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[0][2] ==matrix[1][1] && matrix[1][1] ==matrix[2][0] && matrix[1][1] != false){
            console.log( `Player ${matrix[0][2] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[0][0] ==matrix[1][0] && matrix[1][0] ==matrix[2][0] && matrix[2][0] != false){
            console.log( `Player ${matrix[0][0] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[0][1] ==matrix[1][1] && matrix[1][1] ==matrix[2][1] && matrix[2][1] != false){
            console.log( `Player ${matrix[0][1] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[0][2] ==matrix[1][2] && matrix[1][2] ==matrix[2][2] && matrix[2][2] != false){
            console.log(`Player ${matrix[0][2] } wins!`)
            printBoard(matrix)
            isWin = true
            break
        }else if(matrix[0].every(x => x != false) &&
        matrix[1].every(x => x != false) &&
        matrix[2].every(x => x != false)
        ){
            console.log( "The game ended! Nobody wins :(")
            printBoard(matrix)
            isWin = true
            break
        }
        
    }
   if(isWin==false){
    console.log( "The game ended! Nobody wins :(")
   }
    
}


solve(["0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 1",
    "1 2",
    "2 2",
    "2 1",
    "0 0"]
)

