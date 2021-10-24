function solve (input, criteria){
    let employees
    try {
        employees = JSON.parse(input);
    } catch (error) {
        employees = [];
    }
    
    function formating(employees){
        result = []
        for(let i = 0; i< employees.length; i++){
            result.push(`${i}. ${employees[i].first_name} ${employees[i].last_name} - ${employees[i].email}`)
        }
        return result
    }
    if(criteria=='all'){
        return formating(employees).join('\n')
    }else{
        let [key, value] = criteria.split('-')
        employees = employees.filter(x=> x[key]==value)
        return formating(employees).join('\n')
    }
  
}

console.log( solve(`[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`, 'gender-Female'
))