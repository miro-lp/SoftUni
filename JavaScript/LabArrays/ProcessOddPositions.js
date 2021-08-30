function solve(input){

    let arr = []
    for (let i = 1; i<input.length; i+=2){
        arr.push(input[i])
    }
    let arr1 = arr.map(x=>x*2)
    

    return arr1.reverse().join(' ')
}

console.log(solve([10, 15, 20, 25]))