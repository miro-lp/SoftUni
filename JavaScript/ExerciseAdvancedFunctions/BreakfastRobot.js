function solution (){
    const store ={
        'protein':0,
        'carbohydrate':0,
        'fat':0,
        'flavour':0,
    }
    const recepes = {
        'apple' : {'carbohydrate':1, 'flavour':2},
        'lemonade' : {'carbohydrate':10, 'flavour':20},
        'burger' : {'carbohydrate':5,'fat':7, 'flavour':3 },
        'eggs' : {'protein':5,'fat':1, 'flavour':1 },
        'turkey' : {'protein':10, 'carbohydrate':10,'fat':10 , 'flavour':10},
    }
    function solve(input){

        if(input == 'report'){
            let result = []
            for (let incrd in store){
                result.push(`${incrd}=${store[incrd]}`)
            }
            return result.join(' ')
        }else{
            let [command, position1, quantity] = input.split(' ')
            if(command== 'restock'){
                store[position1]+=Number(quantity)
                return 'Success'
            }else if (command =='prepare'){
                for(let element in recepes[position1]){
                    if(recepes[position1][element]*quantity>store[element]){
                        return `Error: not enough ${element} in stock`
                    }else{
                        store[element]-=recepes[position1][element]*quantity
                    }
                }
                return 'Success'
            }

        }

    }

    return solve

}

let manager = solution (); 
console.log (manager ('prepare turkey 1')); 
console.log (manager ("prepare lemonade 4")); 
console.log (manager ("report")); 