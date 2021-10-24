function focused() {
    let divElements = document.querySelector('div')
    divElements.addEventListener('focus',(e)=>{
        if (e.target.tagName == 'INPUT'){
            e.target.parentElement.className = 'focused'
        }
    })
    divElements.addEventListener('blur',(e)=>{
        if (e.target.tagName == 'INPUT'){
            e.target.parentElement.className = ''
        }
    })

}