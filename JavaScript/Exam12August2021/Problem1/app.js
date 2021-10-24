window.addEventListener('load', solve);

function solve(e) {
    
    let modelElement = document.getElementById('model')
    let yearElement = document.getElementById('year')
    let descriptionElement = document.getElementById('description')
    let priceElement = document.getElementById('price')
    let totalPriceElement = document.getElementsByClassName('total-price')[0]
    let totalPrice = 0
    
    document.getElementById('add').addEventListener('click',function(e){
        e.preventDefault()
        let table = document.getElementById('furniture-list')
        let model = modelElement.value
        let description = descriptionElement.value
        let trElement1 = document.createElement('tr')
        trElement1.classList.add('info')
        let tdModelElement = document.createElement('td')
        let tdPriceElement = document.createElement('td')
        let tdButtonElement = document.createElement('td')
        let butttonMore = document.createElement('button')
        butttonMore.classList.add('moreBtn')
        butttonMore.textContent = 'More Info'
        butttonMore.addEventListener('click', function(){
            if(butttonMore.textContent == 'More Info'){
            trElement2.style.display = 'contents'
            butttonMore.textContent = 'Less Info'
        }else{
                trElement2.style.display = 'none'
                butttonMore.textContent = 'More Info'
            }
        })

        let butttonBuy = document.createElement('button')
        butttonBuy.classList.add('buyBtn')
        butttonBuy.textContent = 'Buy it'
        butttonBuy.addEventListener('click', function(){
            totalPrice += Number(tdPriceElement.textContent)
            totalPriceElement.textContent = totalPrice.toFixed(2)
            trElement1.remove()
            trElement2.remove()
        } )

        tdButtonElement.appendChild(butttonMore)
        tdButtonElement.appendChild(butttonBuy)
        let trElement2 = document.createElement('tr')
        trElement2.classList.add('hide')
        let tdYearElement = document.createElement('td')
        let tdDescriptElement = document.createElement('td')
        tdDescriptElement.colSpan = '3'

        if(Number(yearElement.value)>0 && Number(priceElement.value)>0 &&
        typeof(model)=='string' && typeof(description) == 'string' &&
        model != '' && description != ''){
            tdModelElement.textContent = model
            tdPriceElement.textContent = Number(priceElement.value).toFixed(2)
            trElement1.appendChild(tdModelElement)
            trElement1.appendChild(tdPriceElement)
            trElement1.appendChild(tdButtonElement)

            tdYearElement.textContent = `Year: ${Number(yearElement.value)}`
            tdDescriptElement.textContent = `Description: ${description}`
            trElement2.appendChild(tdYearElement)
            trElement2.appendChild(tdDescriptElement)
            table.appendChild(trElement1)
            table.appendChild(trElement2)
            modelElement.value =''
            yearElement.value ='' 
            descriptionElement.value ='' 
            priceElement.value =''
        }
    })
}
