function solve() {

    document.querySelectorAll('tfoot tr td button')[0].style.cursor = 'pointer'
    document.querySelectorAll('tfoot tr td button')[1].style.cursor = 'pointer'
    document.querySelectorAll('tfoot tr td button')[0].addEventListener('click',()=>{
        let numbersInput = Array.from(document.querySelectorAll('tbody tr td input')).map(x => x.value)
        if (numbersInput[0]!=numbersInput[1] && numbersInput[1]!=numbersInput[2] && numbersInput[0]!=numbersInput[2] &&
            numbersInput[3]!=numbersInput[4] && numbersInput[4]!=numbersInput[5] && numbersInput[3]!=numbersInput[5] &&
            numbersInput[6]!=numbersInput[7] && numbersInput[7]!=numbersInput[8] && numbersInput[6]!=numbersInput[8] &&
            numbersInput[0]!=numbersInput[3] && numbersInput[3]!=numbersInput[6] && numbersInput[0]!=numbersInput[6] &&
            numbersInput[1]!=numbersInput[4] && numbersInput[4]!=numbersInput[7] && numbersInput[1]!=numbersInput[7] &&
            numbersInput[2]!=numbersInput[5] && numbersInput[5]!=numbersInput[8] && numbersInput[2]!=numbersInput[8]
            ){
                document.querySelector('table').style.border = '2px solid green'
                document.querySelector('#check p').textContent = 'You solve it! Congratulations!' 
                document.querySelector('#check p').style.color = 'green' 
            }else{
                document.querySelector('table').style.border = '2px solid red'
                document.querySelector('#check p').textContent = 'NOP! You are not done yet...'
                document.querySelector('#check p').style.color = 'red'
            }
    
    })
    document.querySelectorAll('tfoot tr td button')[1].addEventListener('click',()=>{
        let numbersInput = Array.from(document.querySelectorAll('tbody tr td input')).map(x => x.value='')
        document.querySelector('table').style.border = 'none'
        document.querySelector('#check p').textContent = ''

    })
    

}