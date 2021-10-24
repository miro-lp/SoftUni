function toggle() {
    console.log(document.querySelector('body div div span').textContent)
    if(document.querySelector('body div div span').textContent == 'More'){
    document.getElementById('extra').style.display = 'block'
    document.querySelector('body div div span').textContent = 'Less'
    }else if(document.querySelector('body div div span').textContent == 'Less'){
    document.getElementById('extra').style.display = 'none'
    document.querySelector('body div div span').textContent = 'More'}  
}