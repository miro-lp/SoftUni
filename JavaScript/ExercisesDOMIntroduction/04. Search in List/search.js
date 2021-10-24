function search() {
   let searchText = document.getElementById('searchText').value
   let re = new RegExp(searchText, 'i')
   let list = document.querySelectorAll('ul li')
   let result = 0
   for (let word of list){
      word.style.fontWeight =''
      word.style.textDecoration = ''
      string = word.textContent
      if(re.exec(string)!= null){
         result+=1
         word.style.fontWeight ='bold'
         word.style.textDecoration = 'underline'
      }
   }
   document.getElementById('result').textContent = `${result} matches found`
}
