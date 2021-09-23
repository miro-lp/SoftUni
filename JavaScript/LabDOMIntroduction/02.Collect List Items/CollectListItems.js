function extractText() {
    let itemNodes = document.querySelectorAll('#items li')
    let textarea = document.querySelector('#result')
    let result = ''
    for (let node  of itemNodes){
        node.textContent.trim()
        result +=  node.textContent.trim() + "\n"
    }
    textarea.value = result.trim()
}