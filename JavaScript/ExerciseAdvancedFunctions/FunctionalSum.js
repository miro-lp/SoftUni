function add(num){
    let sum = 0
    sum +=num
    
    function inner(num){
        sum+=num
        
        
        return inner

    }
    inner.toString = ()=> sum
    return inner   
}


console.log(add(1)(6)(-3))