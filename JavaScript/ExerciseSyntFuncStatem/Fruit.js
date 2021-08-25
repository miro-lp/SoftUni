function fruit(fruit, weight, cost){
    let price = (weight*cost)/1000;
    console.log(`I need \$${price.toFixed(2)} to buy ${(weight/1000).toFixed(2)} kilograms ${fruit}.`)
}

fruit('orange', 2500, 1.80)
fruit('apple', 1563, 2.35)