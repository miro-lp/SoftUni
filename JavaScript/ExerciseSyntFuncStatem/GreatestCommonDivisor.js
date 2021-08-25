function commonDivisor(num1, num2) {
    let divisor = 1;

    for (let i = 1; i <= num2; i++) {
        if (num1 % i == 0 && num2 % i == 0) {
            divisor = i
        }

    }

    return divisor
}

console.log(commonDivisor(15, 5))
console.log(commonDivisor(2154, 458))