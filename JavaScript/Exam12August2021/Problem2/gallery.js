class ArtGallery {
    constructor(creator) {
        this.creator = creator
        this.possibleArticles = { "picture": 200, "photo": 50, "item": 250 }
        this.listOfArticles = []
        this.guests = []
    }
    addArticle(articleModel, articleName, quantity) {
        articleModel = articleModel.toLocaleLowerCase()
        if (!Object.keys(this.possibleArticles).includes(articleModel)) {
            throw Error('This article model is not included in this gallery!')
        }
        for (let article of this.listOfArticles) {
            if (Object.values(article)[0] == articleModel && Object.values(article)[1] == articleName) {
                article['quantity'] += quantity
                return `Successfully added article ${articleName} with a new quantity- ${quantity}.`
            }
        }
        this.listOfArticles.push({ articleModel, articleName, quantity })

        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`
    }

    inviteGuest(guestName, personality) {
        for (let guest of this.guests) {
            if (Object.values(guest).includes(guestName)) {
                throw Error(`${guestName} has already been invited.`)
            }
        }
        let points = 0
        if (personality == 'Vip') {
            points = 500
        } else if (personality == 'Middle') {
            points = 250
        } else {
            points = 50
        }

        this.guests.push({
            'guestName': guestName,
            'points': points,
            'purchaseArticle': 0
        })

        return `You have successfully invited ${guestName}!`
    }
    buyArticle(articleModel, articleName, guestName) {
        let isPresent = false
        for (let article of this.listOfArticles) {
            if (Object.values(article)[0] == articleModel && Object.values(article)[1] == articleName) {
                isPresent = true
                if (article['quantity'] == 0) {
                    return `The ${articleName} is not available.`
                }
                let isGuestPresent = false
                for (let guest of this.guests) {
                    if (guest['guestName'] == guestName) {
                        isGuestPresent = true
                        if (guest['points'] < this.possibleArticles[articleModel]) {
                            return 'You need to more points to purchase the article.'
                        } else {
                            guest['points'] -= this.possibleArticles[articleModel]
                            article['quantity'] -= 1
                            guest['purchaseArticle'] += 1
                            return `${guestName} successfully purchased the article worth ${this.possibleArticles[articleModel]} points.`
                        }
                    }
                }
                if (!isGuestPresent) {
                    return 'This guest is not invited.'
                }
            }
        }
        if (!isPresent) {
            throw Error('This article is not found.')
        }
    }
    showGalleryInfo (criteria){
        let result = ''
        if (criteria == 'article'){
            result += 'Articles information:\n'
            for (let article of this.listOfArticles) {
                result+=`${article.articleModel} - ${article.articleName} - ${article.quantity}\n`
            } 
        }else{
            result += 'Guests information:\n'
            for (let guest of this.guests) {
                result += `${guest.guestName} - ${guest.purchaseArticle}\n`
            }
        }
        return result.trim()
    }
}




const artGallery = new ArtGallery('Curtis Mayfield'); 
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('picture', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
artGallery.buyArticle('picture', 'Mona Liza', 'John');
artGallery.buyArticle('item', 'Ancient vase', 'Peter');
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));

