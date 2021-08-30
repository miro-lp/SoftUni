function solve(input){
    let arr = input.sort((x,y)=>x-y)
    num = Math.floor(arr.length/2)
    return arr.slice(num,arr.length)
}

console.log(solve([20,30, 40,2,10]))