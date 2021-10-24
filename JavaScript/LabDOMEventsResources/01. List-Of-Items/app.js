function addItem() {
    let valueInput = document.getElementById('newItemText').value
    let itemsElemet = document.getElementById('items')
    let newElemnt = document.createElement('li')
    newElemnt.textContent = valueInput
    itemsElemet.appendChild(newElemnt)
    document.getElementById('newItemText').value = ''
}