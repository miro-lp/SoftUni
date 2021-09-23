function solve(arr){
    num = -999999
    let newArr =[]
    for (let i = 0; i<arr.length;i++){
        if (arr[i]>=num){
            num=arr[i]
            newArr.push(num)

        }
    }
    return newArr
}