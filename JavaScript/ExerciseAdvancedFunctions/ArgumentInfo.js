function solve(...input) {
    let result = []
    const dict = {}
    for (let arg of input) {
        let type = typeof (arg)
        if (dict[type] == undefined) {
            dict[type] = 0
        }
        dict[type]+=1
        result.push(`${type}: ${arg}`)
    }
    let sortedList = Object.entries(dict).sort((a, b) => b[1] - a[1])
    for (let info of sortedList) {
        result.push(`${info[0]} = ${info[1]}`)
    }
    for (let el of result) {
        console.log(el)
    }

}


solve('cat', 42, function () { console.log('Hello world!'); })
solve({ name: 'bob' }, 3.333, 9.999)