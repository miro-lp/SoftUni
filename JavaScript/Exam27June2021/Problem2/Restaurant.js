class Restaurant {
    constructor(budgetMoney) {
        this.budgetMoney = budgetMoney
        this.menu = {}
        this.stockProducts = {}
        this.history = []
    }

    loadProducts(products) {
        
        for (let product of products) {
            let [productName, quantity, price] = product.split(' ')
            price = Number(price)
            quantity = Number(quantity)
            if (price <= this.budgetMoney) {
                this.budgetMoney -= price
                if (!Object.keys(this.stockProducts).includes(productName)) {
                    this.stockProducts[productName] = 0
                }
                this.stockProducts[productName] += quantity
                this.history.push(`Successfully loaded ${quantity} ${productName}`)
            } else {
                this.history.push(`There was not enough money to load ${quantity} ${productName}`)
            }
        }
        return this.history.join('\n')
    }

    addToMenu(meal, neededProducts, price) {
        if (Object.keys(this.menu).includes(meal)) {
            return `The ${meal} is already in the our menu, try something different.`
        }

        this.menu[meal] = {'name':meal, 'products': {}, 'price': price }
        for (let product of neededProducts) {
            let [productName, productQuantity] = product.split(' ')
            let neededProduct = {}
            neededProduct[productName] = Number(productQuantity)
            Object.assign(this.menu[meal].products, neededProduct)
        }
        if (Object.keys(this.menu).length == 1) {
            return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`
        } else {
            return `Great idea! Now with the ${meal} we have ${Object.keys(this.menu).length} meals in the menu, other ideas?`
        }
    }
    showTheMenu() {
        if (Object.keys(this.menu).length == 0) {
            return "Our menu is not ready yet, please come later..."
        }
        let result = []
        for (let meal of Object.keys(this.menu)) {
            result.push(`${meal} - $ ${this.menu[meal].price}`)
        }
        return result.join('\n')
    }
    makeTheOrder(meal) {
        if (!Object.keys(this.menu).includes(meal)) {
            return `There is not ${meal} yet in our menu, do you want to order something else?`
        }
        for (let product in this.menu[meal].products) {
            if (!Object.keys(this.stockProducts).includes(product) ||
                this.menu[meal].products[product] > this.stockProducts[product]) {
                return `For the time being, we cannot complete your order (${meal}), we are very sorry...`
            }
        }

        for (let product in this.menu[meal].products) {
            if (Object.keys(this.stockProducts).includes(product) &&
                this.menu[meal].products[product] <= this.stockProducts[product]) {
                this.stockProducts[product] -= this.menu[meal].products[product]
            }
        }
        this.budgetMoney += this.menu[meal].price
        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${this.menu[meal].price}.`

    }
}

let kitchen = new Restaurant(1000);
kitchen.loadProducts(['Yogurt 30 3', 'Honey 50 4', 'Strawberries 20 10', 'Banana 5 1']);
kitchen.addToMenu('frozenYogurt', ['Yogurt 1', 'Honey 1', 'Banana 1', 'Strawberries 10'], 9.99);
console.log(kitchen.makeTheOrder('frozenYogurt'));
