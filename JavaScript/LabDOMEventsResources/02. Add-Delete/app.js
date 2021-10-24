function addItem() {
    let valueInput = document.getElementById('newItemText').value
    let itemsElemet = document.getElementById('items')
    let newElemnt = document.createElement('li')
    newElemnt.textContent = valueInput
    let deleteElent = document.createElement('a')
    deleteElent.textContent = '[Delete]'
    deleteElent.setAttribute('href','#')
    deleteElent.addEventListener('click',function(){
        newElemnt.remove()
    })
    newElemnt.appendChild(deleteElent)
    itemsElemet.appendChild(newElemnt)
    document.getElementById('newItemText').value = ''
}