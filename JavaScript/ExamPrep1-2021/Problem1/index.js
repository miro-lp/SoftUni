function solve() {  
    function el(type, attr, ...content) {
        const element = document.createElement(type)
        for (let prop in attr) {
            if (prop == 'class') {
                element.classList.add(attr[prop])
            }else{
                element[prop]=attr[prop]
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


    let [lName, lDate] = document.querySelectorAll('form input')
    let lModule = document.querySelector('select')
    let addButtton = document.querySelector('form button')
    let lectures = {}
    let trainings = document.querySelector('section div')
    addButtton.addEventListener('click', (e) => {
        e.preventDefault()
        let name = lName.value
        let date = lDate.value
        let module = lModule.value

        if (name == '' || module == 'Select module' || date == '') {
            return
        }
        trainings.textContent = ''
        if (!Object.keys(lectures).includes(module)) {
            lectures[module] = []
        }
        lectures[module].push({name, date})
        lectures[module].sort((a,b)=>a.date.localeCompare(b.date))
        for (let m in lectures){

            let divElement = trainings.appendChild(el('div',{class:'module'}, el('h3',{},`${m.toUpperCase()}-MODULE`),
            el('ul',{},'')))
            for (let l of lectures[m]){
                let [day,hour]=l.date.split('T')
                day = day.split('-').join('/')
                let delButton = el('button',{class:'red'},'Del')
                let liElement = (el('li',{class:'flex'},el('h4',{},`${l.name} - ${day} - ${hour}`),delButton))
                delButton.addEventListener('click',()=>{
                    lectures[m].splice(lectures[m].indexOf(l),1)
                    if(lectures[m].length == 0){
                        liElement.parentNode.parentNode.remove()

                    }else{liElement.remove()}
                    
                })
               
                divElement.querySelector('ul').appendChild(liElement)
            }
            
        }

    })

};