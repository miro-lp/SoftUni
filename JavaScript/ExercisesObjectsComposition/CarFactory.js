function solve(input) {
    const car = {}

    car.model = input.model
    if (input.power <= 90) {
        car.engine = { power: 90, volume: 1800 }
    } else if (input.power <= 120) {
        car.engine = { power: 120, volume: 2400 }
    } else {
        car.engine = { power: 200, volume: 3500 }
    }
    car.carriage = { type: input.carriage, color: input.color }
    car.wheels = input.wheelsize % 2 == 0 ? Array(4).fill(input.wheelsize - 1) : Array(4).fill(input.wheelsize)

    return car
}

console.log(solve({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}
))