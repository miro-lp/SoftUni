function solve (input){

    function sortFunc(a,b){
        if (a.length - b.length>0){

            return 1
        }
        if (a.length - b.length<0){

            return -1
        }
        return a.localeCompare(b)
        
    }
    input.sort(sortFunc)
    return input.join('\n')

}

console.log(solve(['test', 
'Deny', 
'omen', 
'Default']
))