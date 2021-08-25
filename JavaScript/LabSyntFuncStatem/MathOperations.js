function mathOperations(a,b, operator){
    let result;
    if (operator=='+'){
        result = a+b
    }else if(operator=='-'){
        result = a-b
    }else if(operator=='*'){
        result = a*b
    }else if(operator=='/'){
        result = a/b
    }else if(operator=='%'){
        result = a%b
    }else if(operator=='**'){
        result = a**b
    }
    console.log(result)
};

mathOperations(5,6,'+')
mathOperations(3,5.5,'*')