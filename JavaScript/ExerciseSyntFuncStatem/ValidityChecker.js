function validityChecker(x1,y1,x2,y2){
    function solve (x1,y1,x2,y2){
        let x = Math.abs(x1-x2)
        let y = Math.abs(y1-y2)
        let l = Math.sqrt(x**2+y**2)
        if (Number.isInteger(l)){
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`)
        }else{
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`)
        }
    }
    solve(x1,y1,0,0)
    solve(x2,y2,0,0)
    solve(x1,y1,x2,y2)
}
validityChecker(3,0,0,4)