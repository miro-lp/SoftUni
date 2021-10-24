function create(words) {
   for (let word of words){
      let newElement = document.createElement('div')
      let paragElemetn = document.createElement('p')
      paragElemetn.textContent = word
      paragElemetn.style.display = 'none'
      newElement.appendChild(paragElemetn)
      newElement.addEventListener('click',(e)=>{
         e.target.children[0].style.display = ''

      })
      document.getElementById('content').appendChild(newElement)
   }
}