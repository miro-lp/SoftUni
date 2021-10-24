class List {
    constructor() {
        this.store = []
        this.size = 0

    }

    add(element) {
        this.store.push(element);
        this.size += 1;
        this.store.sort((a, b) => a - b);
    }
    remove(index) {
        if (index < 0 || index >= this.size) {
            throw Error('Index out of range')
        }

        this.store.splice(index, 1);
        this.size -= 1;
    }

    get(index) {
        if (index < 0 || index >= this.size) {
            throw Error('Index out of range')
        }
        return this.store[index];
    }


}

let list = new List();
list.add(7);
list.add(9);
list.add(4);
list.add(5);
list.add(6);

console.log(list.get(1));
list.remove(1);
console.log(list.get(1));
console.log(list.get(2));
console.log(list.get(3));
console.log(list.size);
