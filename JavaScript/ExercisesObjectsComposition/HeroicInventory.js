function solve(input){
    const heros =[]
    for (let info of input){
    [name, level, items] = info.split(' / ')
    items = items? items.split(', '):[]
    heros.push({'name':name, 'level': Number(level),'items': items })
    }
    return JSON.stringify(heros)
}

console.log(solve(['Isacc / 25 / Apple, GravityGun',
'Derek / 12 / BarrelVest, DestructionSword',
'Hes / 1 / Desolator, Sentinel, Antara']
))