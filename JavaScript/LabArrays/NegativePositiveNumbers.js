function solve(input) {
    let newArray=[]
    for (let i = 0; i < input.length; i++) {
        if (input[i]<0) {
            newArray.unshift(input[i])
        }else{
            newArray.push(input[i])
        }
    }
    return newArray.join('\n')
}
console.log(solve([7, -2, 8, 9]))