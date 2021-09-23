function solve(matrix){
    magicSum = 0
    
    for(let i = 0; i <matrix.length; i ++){
        let sumRow =0
        for(let j = 0 ; j<matrix[i].length; j++){
            sumRow +=matrix[i][j]
        }
        if (magicSum == 0 ){
            magicSum = sumRow
        }
        if (sumRow != magicSum){
            return false
        
        }
    }   
    for(let i = 0; i <matrix[0].length; i ++){
        let sumCol=0
        for(let j = 0 ; j<matrix.length; j++){
                sumCol+=matrix[j][i]
            }
     
        if (sumCol!= magicSum){
                return false
            }
    
    }   
    
    return true
}

console.log(solve([[4, 5, 6],[6, 5, 4],[5, 5, 5]]))