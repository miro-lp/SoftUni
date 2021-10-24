function solve (input){
    const products = {}
    for( let info of input){
        [town, product, price] = info.split(' | ')
        price = Number(price)
        if(!products[product]){  
        products[product]={} 
        }
        products[product][town]=price
    }
    const finalProducts={}
    for( let product in products){
        for( let key of Object.keys(products[product])){
            town = key
            price = products[product][town]
            if(!finalProducts[product] || finalProducts[product].price>price){
            finalProducts[product]={town,price}
            }
        }
    }
    for( let product in finalProducts){
        console.log(`${product} -> ${finalProducts[product].price} (${finalProducts[product].town})`)
    }
}

solve(['Sample Town | Sample Product | 1000',
'Sample Town | Orange | 4',
'Sample Town | Peach | 1',
'Sofia | Orange | 3',
'Sofia | Peach | 2',
'New York | Sample Product | 1000.1',
'New York | Burger | 10']
)