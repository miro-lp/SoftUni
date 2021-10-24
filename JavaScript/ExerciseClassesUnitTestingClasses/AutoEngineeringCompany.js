function solve(input){
    const cars = {}
    for(let car of input){
        let[carBrand, carModel, producedCars] = car.split(' | ')
        producedCars = Number(producedCars)
        if(!(carBrand in cars)){
            cars[carBrand]={}
        }
        if(!(carModel in cars[carBrand])){
            cars[carBrand][carModel]=0
        }
        cars[carBrand][carModel] += producedCars
    }

    let result = []
    for(let brand in cars){
        result.push(brand)
        for(let model in cars[brand]){
            result.push(`###${model} -> ${cars[brand][model]}`)
        }
    }

    return result.join('\n')
}


console.log(solve(['Audi | Q7 | 1000',
'Audi | Q6 | 100',
'BMW | X5 | 1000',
'BMW | X6 | 100',
'Citroen | C4 | 123',
'Volga | GAZ-24 | 1000000',
'Lada | Niva | 1000000',
'Lada | Jigula | 1000000',
'Citroen | C4 | 22',
'Citroen | C5 | 10']
))
