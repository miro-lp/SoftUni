function solve() {
    let nameMovie = document.querySelector('input[placeholder="Name"]')
    let hall = document.querySelector('input[placeholder="Hall"]')
    let priceMovie = document.querySelector('input[placeholder="Ticket Price"]')
    document.querySelector('#container button').addEventListener('click', addMovie)
    document.querySelector('#archive>button').addEventListener('click', (e) => {
        let liElements = e.target.parentNode.querySelectorAll('ul li')
        for (let el of liElements) {
            el.remove()
        }
    })
    let archiveElement = document.querySelector('#archive ul')

    
    function archive(e) {
        let oldLi = e.target.parentNode.parentNode
        let ticketCount = e.target.parentNode.children[1].value
        let priceTicket = e.target.parentNode.children[0].textContent
        let nameMovie = e.target.parentNode.parentNode.children[0].textContent
        if (ticketCount=='' || Number(ticketCount)<0) { return }

        let archiveLiElement = document.createElement('li')
        let spanElement = document.createElement('span')
        spanElement.textContent = nameMovie
        archiveLiElement.appendChild(spanElement)
        let strongElemnt = document.createElement('strong')
        strongElemnt.textContent = `Total amount: ${Number(Number(ticketCount) * priceTicket).toFixed(2)}`
        archiveLiElement.appendChild(strongElemnt)
        let buttonElement = document.createElement('button')
        buttonElement.textContent = 'Delete'
        buttonElement.addEventListener('click', (e) => {
            e.target.parentNode.remove()
        })
        archiveLiElement.appendChild(buttonElement)
        archiveElement.appendChild(archiveLiElement)

        oldLi.remove()

    }
    function addMovie(e) {
        e.preventDefault()

        if (nameMovie.value && hall.value && Number(priceMovie.value)) {
            let liElement = document.createElement('li')
            let spanElement = document.createElement('span')
            spanElement.textContent = nameMovie.value
            liElement.appendChild(spanElement)
            let strongElemnt = document.createElement('strong')
            strongElemnt.textContent = `Hall: ${hall.value}`
            liElement.appendChild(strongElemnt)
            let divElement = document.createElement('div')
            let strongDivElement = document.createElement('strong')
            strongDivElement.textContent = Number(priceMovie.value).toFixed(2)
            divElement.appendChild(strongDivElement)
            let divInputElement = document.createElement('input')
            divInputElement.placeholder = 'Tickets Sold'
            divElement.appendChild(divInputElement)
            let divButtonElement = document.createElement('button')
            divButtonElement.textContent = 'Archive'
            divButtonElement.addEventListener('click', archive)
            divElement.appendChild(divButtonElement)
            liElement.appendChild(divElement)
            document.querySelector('#movies ul').appendChild(liElement)
        } else {
            return
        }
        nameMovie.value = ''
        hall.value = ''
        priceMovie.value = ''
    }




}