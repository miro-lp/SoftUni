function solve() {
    function el(type, attr, ...content) {
        const element = document.createElement(type)
        for (let prop in attr) {
            if (prop == 'class') {
                element.classList.add(attr[prop])
            } else {
                element[prop] = attr[prop]
            }
        }
        for (let item of content) {
            if (typeof item == 'string' || typeof item == 'number') {
                item = document.createTextNode(item)
            }
            element.appendChild(item)
        }
        return element
    }

    let [taskEl, dateEl] = document.querySelectorAll('form input')
    let descriptionEl = document.querySelector('form textarea')
    let addButton = document.querySelector('form button')
    let [_, openDiv, progressDiv, completeDiv] = document.querySelectorAll('section div:nth-child(2)')

    let openTasks = []
    let progressTasks = []
    let completeTasks = []

    addButton.addEventListener('click', (e) => {
        e.preventDefault()
        let task = taskEl.value
        let date = dateEl.value
        let description = descriptionEl.value
        if (task == '' || date == '' || description == '') {
            return
        }
        openTasks.push({ task, description, date })
        taskEl.value = ''
        descriptionEl.value = ''
        dateEl.value = ''
        openDiv.textContent = ''
        for (let a of openTasks) {
            let startButton = el('button', { class: 'green' }, 'Start')
            let delButton = el('button', { class: 'red' }, 'Delete')
            delButton.addEventListener('click', () => {
                article.remove()
                openTasks.splice(openTasks.indexOf(a), 1)
            })
            startButton.addEventListener('click', () => {
                progressTasks.push(a)
                article.remove()
                openTasks.splice(openTasks.indexOf(a), 1)
                progressDiv.textContent = ''
                progreessRender(progressTasks)
            })
            let article = el('article', {}, el('h3', {}, a.task), el('p', {}, `Description: ${a.description}`),
                el('p', {}, `Due Date: ${a.date}`), el('div', { class: 'flex' }, startButton, delButton))
            openDiv.appendChild(article)
        }

        function progreessRender(progressTasks) {
            for (let a of progressTasks) {
                let finishButton = el('button', { class: 'orange' }, 'Finish')
                let delButton = el('button', { class: 'red' }, 'Delete')
                delButton.addEventListener('click', () => {
                    article.remove()
                    progressTasks.splice(progressTasks.indexOf(a), 1)
                })
                finishButton.addEventListener('click', () => {
                    completeTasks.push(a)
                    article.remove()
                    progressTasks.splice(progressTasks.indexOf(a), 1)
                    completeDiv.textContent = ''
                    completeRender(completeTasks)
                })
                let article = el('article', {}, el('h3', {}, a.task), el('p', {}, `Description: ${a.description}`),
                    el('p', {}, `Due Date: ${a.date}`), el('div', { class: 'flex' }, delButton, finishButton))
                progressDiv.appendChild(article)
            }
        }

        function completeRender(completeTasks) {
            for (let a of completeTasks) {
                let article = el('article', {}, el('h3', {}, a.task), el('p', {}, `Description: ${a.description}`),
                    el('p', {}, `Due Date: ${a.date}`))
                completeDiv.appendChild(article)
            }
        }
    })

}