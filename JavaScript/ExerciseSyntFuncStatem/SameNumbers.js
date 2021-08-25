function sameNumbers(num){
    num = String(num);
    let result = 0;
    let isSame = false;
    const set1 = new Set(num)
    if (set1.size==1){
        isSame = true
    }

    for (let i=0; i<num.length; i++){
        result +=Number(num[i])
        

    }
    console.log(isSame)
    console.log(result)

}

sameNumbers(2222222)
sameNumbers(1234)