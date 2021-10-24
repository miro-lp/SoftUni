function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchText = document.getElementById('searchField').value
      let re = new RegExp(searchText, 'i')
      let list = Array.from(document.querySelectorAll('table tbody tr td'))
      list.forEach(x => {x.parentElement.className = ''})

      for (let word of list){
         string = word.textContent
         if(re.exec(string)!= null){
            
            word.parentElement.className = 'select'
         }
      }
      
   }
}