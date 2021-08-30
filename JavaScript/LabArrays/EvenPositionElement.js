function solve(input) {
    let newArray=[]
    for (let i = 0; i < input.length; i++) {
        if (i % 2 == 0) {
            newArray.push(input[i])

        }
    }
    return newArray.join(' ')
}

console.log(solve([20,30, 40,50,60]))