function solve(arr,n){
    for(let i =0; i<n;i++){
        num = arr.pop()
        arr.unshift(num)
    }
    return arr.join(' ')
}
console.log(solve(['1','2','3','4'],2))

    