function sumTable() {
    let rows = document.querySelectorAll('table tbody tr td:nth-child(2)') 
    rows = Array.from(rows)
    let result = rows.pop()
    sum = 0
    for (let row of rows){
        sum += Number(row.textContent)
        }
    result.textContent = sum  
}