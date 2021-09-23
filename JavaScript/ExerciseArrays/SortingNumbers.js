function solve(input){
    input.sort((a,b)=>a-b)
    let resultArr = []
    while(input.length>0){
        resultArr.push(input.shift())
        if (input.length>0){
            resultArr.push(input.pop())
        }
    }
    return resultArr
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))

