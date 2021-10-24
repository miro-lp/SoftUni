function attachGradientEvents() {
    let gradient = document.getElementById('gradient')
    gradient.addEventListener('mousemove',function(e){
        let result = Math.trunc((e.offsetX / (e.target.clientWidth - 1))*100);
        document.getElementById('result').textContent = result + '%'
    })
    gradient.addEventListener('mouseout',function(){
        
        document.getElementById('result').textContent = ''
    })
}