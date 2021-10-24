function addItem() {
    let textElement = document.getElementById('newItemText')
    let valueElement = document.getElementById('newItemValue')

    let newElement = document.createElement('option')
    newElement.textContent = textElement.value
    newElement.value = valueElement.value

    document.getElementById('menu').appendChild(newElement)
    textElement.value = ''
    valueElement.value = ''


}