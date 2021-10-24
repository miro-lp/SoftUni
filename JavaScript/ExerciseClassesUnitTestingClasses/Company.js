class Company {
    constructor(){
        this.departments = {}
    }
    addEmployee(name, salary, position, department){

        if(name ==  undefined || name == '' || name == null ||
        salary == undefined || salary == '' || salary == null || salary < 0 ||
        position ==  undefined || position == '' || position == null || 
        department ==  undefined || department == '' || department == null){
            throw Error('Invalid input!')
        }
        if (!(department in this.departments)){
            this.departments[department]=[]
        }
        this.departments[department].push({name, salary, position})
        return `New employee is hired. Name: ${name}. Position: ${position}`
    }

    bestDepartment(){
        let avarageSalary = 0
        let departmentHighSalary =''
        for (let key in this.departments){
            let salaryInProgres = 0
            for(let e of this.departments[key]){
                salaryInProgres += e.salary
            }
            this.departments[key].sort((a,b)=>b.salary - a.salary || a.name.localeCompare(b.name))
            salaryInProgres = salaryInProgres/this.departments[key].length
            if(salaryInProgres>avarageSalary){
                avarageSalary = salaryInProgres
                departmentHighSalary = key
            }
    
        }
        let result = []
        result.push(`Best Department is: ${departmentHighSalary}`)
        result.push(`Average salary: ${avarageSalary.toFixed(2)}`)
        for (let e of this.departments[departmentHighSalary]){
            result.push(`${e.name} ${e.salary} ${e.position}`)
        }

        return result.join('\n')


    }


}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());

