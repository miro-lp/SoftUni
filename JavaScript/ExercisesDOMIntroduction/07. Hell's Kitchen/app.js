function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let input = document.querySelector('#inputs textarea').
      value.slice(1,-2).split('"').map(x => x.trim()).filter(x=> x!='').filter(x=>x != ',')
      const restaurantDict = {}
      for (let info of input){
      let [restaurant, workers] = info.split(' - ')
      if(restaurantDict[restaurant]==undefined){
      restaurantDict[restaurant]={}
      }
      workers = workers.split(', ')
      for (let worker of workers){
         let [name, salary] = worker.split(' ')
         restaurantDict[restaurant][name] = Number(salary)
      }
      
      }
      let bestAvarage = {}
      for(rest in restaurantDict){
         let salary =0
         for(let name in restaurantDict[rest]){
            salary+=restaurantDict[rest][name]
         }
         bestAvarage[rest]=salary/Object.keys(restaurantDict[rest]).length
      
      }
      let items = Object.entries(bestAvarage)
      items.sort((x, y )=> y[1] - x[1])
      console.log(restaurantDict)
      console.log(items)

      let bestSalaries = Object.entries(restaurantDict[items[0][0]])
      bestSalaries.sort((x, y )=> y[1] - x[1])
      console.log(bestSalaries)
      let textOutputWorker =[]
      for(let workerInfo of bestSalaries){
         textOutputWorker.push(`Name: ${workerInfo[0]} With Salary: ${workerInfo[1]}`)
      }

      document.querySelector('#bestRestaurant p').textContent = `Name: ${items[0][0]} Average Salary: ${bestAvarage[items[0][0]].toFixed(2)} Best Salary: ${bestSalaries[0][1].toFixed(2)}`
      document.querySelector('#workers p').textContent = textOutputWorker.join(' ')
   }
}