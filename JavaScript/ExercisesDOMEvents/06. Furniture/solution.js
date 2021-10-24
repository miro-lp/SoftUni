function solve() {

 
  document.querySelector('#exercise button').addEventListener('click',()=>{
    let furnitureText = document.querySelectorAll('#exercise textarea')[0].value
    if(!furnitureText){return}
    let listFurniture = JSON.parse(furnitureText)
    
    for (i=0;i<listFurniture.length; i++){
      let rowElement = document.createElement('tr')
      let imgElement =  document.createElement('img')
      imgElement.src= listFurniture[i].img
      let tdImgElement = document.createElement('td')
      tdImgElement.appendChild(imgElement)
      rowElement.appendChild(tdImgElement)
      let nameElement =  document.createElement('p')
      nameElement.textContent = listFurniture[i].name
      let tdNamenElement = document.createElement('td')
      tdNamenElement.appendChild(nameElement)
      rowElement.appendChild(tdNamenElement)
      let priceElement =  document.createElement('p')
      priceElement.textContent = listFurniture[i].price
      let tdPriceElement = document.createElement('td')
      tdPriceElement.appendChild(priceElement)
      rowElement.appendChild(tdPriceElement)
      let factorElement =  document.createElement('p')
      factorElement.textContent = listFurniture[i].decFactor
      let tdfactorElement = document.createElement('td')
      tdfactorElement.appendChild(factorElement)
      rowElement.appendChild(tdfactorElement)
      let tdMarkElement = document.createElement('td')
      let markElement = document.createElement('input')
      markElement.type="checkbox"
      tdMarkElement.appendChild(markElement)
      rowElement.appendChild(tdMarkElement)
      document.querySelector('tbody').appendChild(rowElement)

  }
    
  })
  document.querySelectorAll('#exercise button')[1].addEventListener('click',()=>{
    let listFurniture = document.querySelectorAll('tbody tr')
    let markedFurniture = []
    for(let furn of listFurniture){
      if(furn.children[4].children[0].checked ==true){
        let name = furn.children[1].textContent
        let price =Number(furn.children[2].textContent)
        let decfactor = Number(furn.children[3].textContent)

        markedFurniture.push({name,price,decfactor})
      }
    }
    let nameFurniture = []
    let totalPrice = 0
    let decfactor = 0
    for (let furniture of markedFurniture){
      nameFurniture.push(furniture.name)
      totalPrice+=furniture.price
      decfactor+=furniture.decfactor
    }
    let totalInfo = `Bought furniture: ${nameFurniture.join(', ')}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${decfactor/markedFurniture.length}`

    document.querySelectorAll('#exercise textarea')[1].value = totalInfo

  })




}