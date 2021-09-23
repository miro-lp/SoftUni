function solve(input){
    input.sort()
    for( let i=1; i<=input.length; i++){
        console.log(`${i}.${input[i-1]}`)
    }
}

solve(["John", "Bob", "Christina", "Ema"])