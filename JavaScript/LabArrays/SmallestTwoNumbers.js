function solve(input){
    let arr = input.sort((x,y)=>x-y)
    return arr.slice(0,2).join(' ')
}

console.log(solve([20,30, 40,2,10]))