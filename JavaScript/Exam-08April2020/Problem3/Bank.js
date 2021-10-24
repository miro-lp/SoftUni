class Bank {
    constructor(bankName) {
        this._bankName = bankName
        this.allCustomers = []
    }

    newCustomer(customer) {
        if (this.allCustomers.filter(c => c.personalId == customer.personalId).length == 1) {
            throw Error(`${customer.firstName} ${customer.lastName} is already our customer!`)
        }
        customer.transactions = []
        customer.totalMoney = 0
        this.allCustomers.push(customer)
        return customer
    }

    depositMoney(personalId, amount) {
        if (this.allCustomers.filter(c => c.personalId == personalId).length == 0) {
            throw Error(`We have no customer with this ID!`)
        }
        let customer = this.allCustomers.filter(c => c.personalId == personalId)[0]

        customer.totalMoney += amount
        customer.transactions.push(`${customer.firstName} ${customer.lastName} made deposit of ${amount}$!`)
        return `${customer.totalMoney}$`
    }

    withdrawMoney(personalId, amount) {
        if (this.allCustomers.filter(c => c.personalId == personalId).length == 0) {
            throw Error(`We have no customer with this ID!`)
        }
        let customer = this.allCustomers.filter(c => c.personalId == personalId)[0]
        if (customer.totalMoney < amount) {
            throw Error(`${customer.firstName} ${customer.lastName} does not have enough money to withdraw that amount!`)
        }
        customer.totalMoney -= amount
        customer.transactions.push(`${customer.firstName} ${customer.lastName} withdrew ${amount}$!`)
        return `${customer.totalMoney}$`
    }

    customerInfo(personalId) {
        if (this.allCustomers.filter(c => c.personalId == personalId).length == 0) {
            throw Error(`We have no customer with this ID!`)
        }
        let c = this.allCustomers.filter(c => c.personalId == personalId)[0]
        let result = [`Bank name: ${this._bankName}`, `Customer name: ${c.firstName} ${c.lastName}`,
        `Customer ID: ${personalId}`, `Total Money: ${c.totalMoney}$`, `Transactions:`]
        for (let i in c.transactions) {
            result.push(`${c.transactions.length -i}. ${c.transactions[c.transactions.length -1 - i]}`)
        }
        return result.join('\n')
    }
}

let bank = new Bank('SoftUni Bank');

console.log(bank.newCustomer({ firstName: 'Svetlin', lastName: 'Nakov', personalId: 6233267 }));
console.log(bank.newCustomer({ firstName: 'Mihaela', lastName: 'Mileva', personalId: 4151596 }));
console.log(bank.newCustomer({ firstName: 'Svetlin', lastName: 'Nakov', personalId: 6233267 }));
bank.depositMoney(6233267, 250);
console.log(bank.depositMoney(6233267, 250));
bank.depositMoney(4151596, 555);

console.log(bank.withdrawMoney(6233267, 125));

console.log(bank.customerInfo(6233267));
