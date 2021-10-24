window.addEventListener('load', solution);

function solution() {
  let fullName = document.getElementById('fname')
  let email = document.getElementById('email')
  let phoneNumber = document.getElementById('phone')
  let adress = document.getElementById('address')
  let code = document.getElementById('code')
  let listElements = [fullName, email, phoneNumber, adress, code]
  let ulElement = document.getElementById('infoPreview')
  let editElement = document.getElementById('editBTN')
  let continueElement = document.getElementById('continueBTN')
  let submitButton = document.getElementById('submitBTN')
  editElement.addEventListener('click', (e) => {

    editElement.disabled = true
    continueElement.disabled = true
    submitButton.disabled = false
    let listLiElements = Array.from(ulElement.children)
    for(let i =0; i<5; i++){ 
      listElements[i].value = listLiElements[i].textContent.split(': ')[1]
      listLiElements[i].remove()
    }
  })

  continueElement.addEventListener('click',()=>{
    let blockElement = document.getElementById('block')
    Array.from(blockElement.children).forEach(e=>e.remove())
    let head3 = document.createElement('h3')
    head3.textContent = 'Thank you for your reservation!'
    blockElement.appendChild(head3)
  })
  submitButton.addEventListener('click', (e) => {
    if (fullName.value != '' && email.value != '') {
      for (let el of listElements) {
        ulElement.appendChild(createLiElement(el))
        el.value = ''
      }
      e.target.disabled = true
      editElement.disabled = false
      continueElement.disabled = false
    }
  })

  function createLiElement(element) {
    let el = document.createElement('li')
    let parent = element.parentNode
    el.textContent = `${parent.children[0].textContent} ${element.value}`
    return el
  }
}
