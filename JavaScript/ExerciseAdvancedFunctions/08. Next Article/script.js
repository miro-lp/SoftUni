function getArticleGenerator(articles) {
    let articlesClouser = articles
    let articleElement = document.getElementById('content')
    let i = 0

    function solve(){
        if (i<articlesClouser.length){
        let article1 = document.createElement('article')
        article1.textContent = articles[i] 
        articleElement.appendChild(article1)
        i+=1}
    }

    return solve
}
