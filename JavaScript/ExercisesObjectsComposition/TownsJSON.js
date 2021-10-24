function solve(input) {
    const towns = []
    for (let i = 1; i < input.length; i++) {
        let [a, Town, Latitude, Longitude, b] = input[i].split('|')
        Town = Town.slice(1, Town.length - 1)
        Latitude = Math.round((Number(Latitude) + Number.EPSILON) * 100) / 100
        Longitude = Math.round((Number(Longitude) + Number.EPSILON) * 100) / 100
        towns.push({ Town, Latitude, Longitude })
    }
    return JSON.stringify(towns)
}

console.log(solve(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']
))