function solve() {
  let firstParam = document.getElementById('text').value
  let secondParam = document.getElementById('naming-convention').value
  let words = firstParam.split(' ')
  words = words.map(x => x.toLowerCase())
  let result = ''
  if(secondParam=='Camel Case'){
    result+=words[0]
    for(let i = 1; i<words.length; i++){
      let word = words[i].charAt(0).toUpperCase() + words[i].slice(1)
      result += word
    }
  }else if (secondParam=='Pascal Case'){
    for(let i = 0; i<words.length; i++){
      let word = words[i].charAt(0).toUpperCase() + words[i].slice(1)
      result += word
    }

  }else{
    result += 'Error!'
  }
  document.getElementById('result').textContent = result

}