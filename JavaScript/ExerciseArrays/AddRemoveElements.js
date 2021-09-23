function solve(input){
    let num = 1
    let arr =[]
    for (i =0; i< input.length; i++ ){
        if (input[i]=='add'){
            arr.push(num)
        }else{
            arr.pop()
        }
        num +=1
    }
    return arr.length == 0 ? 'Empty' : arr.join('\n')
}