function solve(input){
    input.sort()
    const products = {}
    for (let info of input){
        let [product, price] = info.split(' : ')
        products[product]=price
    }
    const alphabetProducts = {}
    for (let product in products){
        if(!alphabetProducts[product[0]]){
        alphabetProducts[product[0]]={}
        }
        Object.assign(alphabetProducts[product[0]],{[product]:products[product]})

    }
    for (let l in alphabetProducts){
        console.log(l)
        for (product in alphabetProducts[l]){
            console.log(`  ${product}: ${alphabetProducts[l][product]}`)

        }
    }
}

(solve(['Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10']
))