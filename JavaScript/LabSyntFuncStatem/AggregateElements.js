function aggregateElements(args){
    let result = 0;
    for (let i =0; i<args.length; i++){
        result+=args[i]
    }
    console.log(result)
    result=0
    for (let i =0; i<args.length; i++){
        result+=1/args[i]
    }
    console.log(result)
    result=''
    for (let i =0; i<args.length; i++){
        result+=String(args[i])
    }
    console.log(result)
}

aggregateElements([1,2,3])