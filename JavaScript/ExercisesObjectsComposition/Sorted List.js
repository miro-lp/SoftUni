function createSortedList(){
    let store = []
    return {
        size : 0,
        add(num) {store.push(num)
        store.sort((a,b)=> a-b)
        this.size = store.length
    },
        remove(index) {
            if(index<store.length && index>=0){
                store.splice(index,1)
            }
            this.size = store.length
        },
        get(index) {
            return store[index]
        }
    }
}

let list = createSortedList();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1)); 
list.remove(1);
console.log(list.get(1));
