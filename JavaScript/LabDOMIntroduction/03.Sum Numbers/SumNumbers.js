function calc() {
    num1 = document.getElementById('num1')
    num2 = document.getElementById('num2')
    sum = Number(num1.value) + Number(num2.value)
    document.getElementById('sum').value = sum
}
