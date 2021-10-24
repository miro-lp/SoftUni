class Stringer{
    constructor(innerString, innerLength){
        this.innerString = innerString
        this.innerLength = innerLength
    }

    decrease(length) {
        if (this.innerLength<=length){
            this.innerLength = 0
        }else{
            this.innerLength-=length
        }
    }

    increase(length) {
        this.innerLength += length
    }
    
    toString() {
        if (this.innerLength>=this.innerString.length){
            return this.innerString
        }else{
            return this.innerString.slice(0,this.innerLength)+'...'
        }

    }
}

let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...

test.increase(4); 
console.log(test.toString()); // Test
