class Parking {
    constructor(capacity) {
        this.capacity = capacity
        this.vehicles = []

    }

    addCar(carModel, carNumber) {
        if (this.vehicles.length >= this.capacity) {
            throw Error('Not enough parking space.')
        }
        this.vehicles.push({ carModel, carNumber, payed: false })
        return `The ${carModel}, with a registration number ${carNumber}, parked.`
    }

    removeCar(carNumber) {
        if (this.vehicles.filter(c => c.carNumber == carNumber).length == 0) {
            throw Error('The car, you\'re looking for, is not found.')
        }
        let car = this.vehicles.filter(c => c.carNumber == carNumber)[0]
        if (car.payed == false) {
            throw Error(`${carNumber} needs to pay before leaving the parking lot.`)
        }
        this.vehicles.splice(this.vehicles.indexOf(car), 1)
        return `${carNumber} left the parking lot.`
    }

    pay(carNumber) {
        if (this.vehicles.filter(c => c.carNumber == carNumber).length == 0) {
            throw Error(`${carNumber} is not in the parking lot.`)
        }
        let car = this.vehicles.filter(c => c.carNumber == carNumber)[0]
        if (car.payed == true) {
            throw Error(`${carNumber}'s driver has already payed his ticket.`)
        }
        car.payed = true
        return `${carNumber}'s driver successfully payed for his stay.`
    }

    getStatistics(carNumber) {
        let result = []
        if (carNumber == undefined) {
            result.push(`The Parking Lot has ${this.capacity - this.vehicles.length} empty spots left.`)
            this.vehicles.sort((a,b)=>a.carModel.localeCompare(b.carModel))
            for(let v of this.vehicles){
                result.push(`${v.carModel} == ${v.carNumber} - ${v.payed == true ? 'Has payed': 'Not payed'}`)
            }
        } else {
            let v = this.vehicles.filter(c => c.carNumber == carNumber)[0]
            result.push(`${v.carModel} == ${v.carNumber} - ${v.payed == true ? 'Has payed': 'Not payed'}`)
        }
        return result.join('\n')
    }
}

const parking = new Parking(12);

console.log(parking.addCar("Volvo t600", "TX3691CA"));
console.log(parking.getStatistics());

console.log(parking.pay("TX3691CA"));
console.log(parking.getStatistics("TX3691CA"));
console.log(parking.removeCar("TX3691CA"));
