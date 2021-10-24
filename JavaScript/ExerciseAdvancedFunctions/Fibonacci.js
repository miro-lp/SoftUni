function getFibonator(){
    let numbers = [0]
    function solve(){
        let num;
        if (numbers.length == 1){
            num=1
            numbers.push(num)
        }else{
        num = numbers[numbers.length-2]+numbers[numbers.length-1]
        numbers.push(num)
        }
        return num
    }
    return solve
}

let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); // 13
