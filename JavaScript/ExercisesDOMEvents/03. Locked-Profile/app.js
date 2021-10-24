function lockedProfile() {
    let mainElement = document.getElementById('main')
    
    mainElement.addEventListener('click',(e)=>{
        if (e.target.tagName == 'BUTTON' ){
            let radioButton = e.target.parentElement.querySelector('div input[value="unlock"]')
            let hiddenElement =e.target.parentElement.querySelector('div') 
            if(radioButton.checked == true){
                if(hiddenElement.style.display == 'none'){
            hiddenElement.style.display = 'inline-block'
            e.target.textContent = 'Hide it'}else{
                hiddenElement.style.display = 'none'
            e.target.textContent = 'Show more'
            }   
        }

        }
    })


}