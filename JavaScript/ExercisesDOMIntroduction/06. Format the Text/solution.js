function solve() {
  let textArea = document.getElementById('input').value.split('.').filter(x => x !== '').map(x => x + '.')

  let sentenceRoof = Math.ceil(textArea.length / 3)

  for (let i = 0; i < sentenceRoof; i++) {
    document.getElementById('output').innerHTML += `<p>${textArea.splice(0, 3).join(' ')}</p>`
  }

}