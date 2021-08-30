function solve(arr, text1, text2) {
    index1 = arr.indexOf(text1)
    index2 = arr.indexOf(text2) + 1
    return arr.slice(index1, index2)
}

