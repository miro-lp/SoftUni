function solve(numbers, command){
    if(command=='asc'){
        function sorting(a,b){
            return a-b
        }
    }else{
        function sorting(a,b){
            return b-a
        }
    }
    return numbers.sort(sorting)
}

console.log(solve([14, 7, 17, 6, 8], 'asc'))
console.log(solve([14, 7, 17, 6, 8], 'desc'))