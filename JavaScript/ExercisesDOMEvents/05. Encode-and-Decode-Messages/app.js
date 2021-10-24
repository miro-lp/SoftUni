function encodeAndDecodeMessages() {
    let [messageElement, receivedMessageElement] = Array.from(document.querySelectorAll('#main div'))
    
    messageElement.querySelector('button').addEventListener('click', () => {
        let message = messageElement.querySelector('textarea').value
        let result = ''
        for (i = 0; i < message.length; i++) {
            result += String.fromCharCode(message[i].charCodeAt(0) + 1)
            
        }
        messageElement.querySelector('textarea').value = ''
        receivedMessageElement.querySelector('textarea').value= result
    })
    
    receivedMessageElement.querySelector('button').addEventListener('click', () => {
        let message = receivedMessageElement.querySelector('textarea').value
        let result = ''
        for (i = 0; i < message.length; i++) {
            result += String.fromCharCode(message[i].charCodeAt(0) -1)
            
        } 

        
        receivedMessageElement.querySelector('textarea').value= result

    })
    

}