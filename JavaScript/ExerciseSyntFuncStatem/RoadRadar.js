function radar(speed, area) {

    function status(limit, speed) {
        let status = '';
        if (speed - limit <= 20) {
            status = 'speeding'
        } else if (speed - limit <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }
        return status
    }
    if (area == 'motorway') {

        if (speed <= 130) {
            return `Driving ${speed} km/h in a 130 zone`
        } else {

            return `The speed is ${speed - 130} km/h faster than the allowed speed of 130 - ${status(130, speed)}`
        }
    } else if (area == 'interstate') {
        if (speed <= 90) {
            return `Driving ${speed} km/h in a 90 zone`
        } else {
            return `The speed is ${speed - 90} km/h faster than the allowed speed of 90 - ${status(90, speed)}`
        }
    } else if (area == 'city') {
        if (speed <= 50) {
            return `Driving ${speed} km/h in a 50 zone`
        } else {
            return `The speed is ${speed - 50} km/h faster than the allowed speed of 50 - ${status(50, speed)}`
        }
    } else {
        if (speed <= 20) {
            return `Driving ${speed} km/h in a 20 zone`
        } else {
            return `The speed is ${speed - 20} km/h faster than the allowed speed of 20 - ${status(20, speed)}`
        }
    }
}

console.log(radar(21, 'residential'))