function solve(area, vol, input) {
    let result = []
    input = JSON.parse(input)
    for (let coodinate of input) {
        let ojb = {}
        result.push({
            'area': area.call(coodinate), 'volume': vol.call(coodinate)
        })
    }
    return result
}

function area() {
    return Math.abs(this.x * this.y);
};

function vol() {
    return Math.abs(this.x * this.y * this.z);
};


console.log(solve(area, vol, '[{"x":"1","y":"2","z":"10"}, {"x":"7","y":"7","z":"10"},{"x":"5","y":"2","z":"10"}]'
))