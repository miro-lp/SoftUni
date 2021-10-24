function solve(arr, criteria) {
    arr.forEach((item, index, arr) => {
        let [a, b, c] = item.split('|')
        b = Number(b)
        arr[index] = [a, b, c];
    });
    if (criteria == 'destination') {
        arr.sort((a, b) => { return a[0].localeCompare(b[0]) })
    } else if (criteria == 'price') {
        arr.sort((a, b) => { return a[1] - b[1] })
    } else {
        arr.sort((a, b) => { return a[2].localeCompare(b[2]) })
    }
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination
            this.price = price
            this.status = status
        }
    }
    result = []

    arr.forEach((e) => {

        result.push(new Ticket(...e))

    })


    return result

}


console.log(solve(['Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed'],
    'status'
))