function solve(input){
    const bottles = {};
    const leftQuantity = {};
    for (let i of input){
        let [juice, quantity] = i.split(' => ');
        quantity = Number(quantity)
        if (!(juice in leftQuantity)){
            leftQuantity[juice] = 0
        }
        leftQuantity[juice] += quantity

        while (leftQuantity[juice]>=1000){

                if (!(juice in bottles)){
                    bottles[juice]=1
                }else{
                    bottles[juice]+=1
                }
                leftQuantity[juice] -= 1000
            
        }
        
    }
    let result = []
    for (let key in bottles){
        result.push(`${key} => ${bottles[key]}`)
    }
    return result.join('\n')
}

console.log(solve(['Orange => 2000',
'Peach => 1432',
'Banana => 450',
'Peach => 600',
'Strawberry => 549']
))
console.log(solve(['Kiwi => 234',
'Pear => 2345',
'Watermelon => 3456',
'Kiwi => 4567',
'Pear => 5678',
'Watermelon => 6789']
))