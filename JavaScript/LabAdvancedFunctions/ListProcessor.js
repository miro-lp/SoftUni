function solve(commands) {
    let result = []
    const commandsObj = {
        add: (value) => result.push(value),
        remove: (value) => result.splice(result.indexOf(value), 1),
        print: () => console.log(result.join(','))
    }
    for (let command of commands) {
        if (command != 'print') {
            let [key, value] = command.split(' ')
            commandsObj[key](value)
        } else {
           commandsObj[command]()
        }

    }
}

solve(['add hello', 'add again', 'remove hello', 'add again', 'print'])