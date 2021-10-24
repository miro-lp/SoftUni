function deleteByEmail() {
    let emailListElements = document.querySelectorAll('#customers tbody tr')
    let emailSearch = document.querySelector('label input').value
    for(let row of emailListElements){
        if(emailSearch == row.querySelector('td:nth-child(2)').textContent){
            row.remove()
            return
        }
    }
    document.getElementById('result').textContent = 'Not found.'
}