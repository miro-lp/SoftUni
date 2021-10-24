class Contact{
    constructor(firstName, lastName, phone, email){
        this.firstName = firstName
        this.lastName = lastName
        this.phone = phone
        this.email = email
        this.online = false
    }
    render(id) {
        
        let articleElement = document.createElement('article');
        let divTitleElement = document.createElement('div');
        divTitleElement.className = 'title';
        divTitleElement.textContent = `${this.firstName} ${this.lastName}`;
        let buttonElement = document.createElement('button');
        buttonElement.textContent = "\u2139";
        
        
        
        let divInfoElement = document.createElement('div');
        divInfoElement.className = 'info';
        divInfoElement.style.display = 'none';
        let spanPhoneElement = document.createElement('span');
        spanPhoneElement.textContent = `\u260E ${this.phone}`;
        divInfoElement.append(spanPhoneElement);
        buttonElement.addEventListener('click',()=>{
            if(divInfoElement.style.display == 'block'){
                divInfoElement.style.display = 'none' 
            }else{
            divInfoElement.style.display = 'block'}
            
        });
        divTitleElement.append(buttonElement);

        let spanEmailElement = document.createElement('span');
        spanEmailElement.textContent = `\u2709 ${this.email}`;

        divInfoElement.append(spanEmailElement);
        articleElement.append(divTitleElement);
        articleElement.append(divInfoElement);
        document.getElementById(`${id}`).append(articleElement);

    }



}

let contacts = [
    new Contact("Ivan", "Ivanov", "0888 123 456", "i.ivanov@gmail.com"),
    new Contact("Maria", "Petrova", "0899 987 654", "mar4eto@abv.bg"),
    new Contact("Jordan", "Kirov", "0988 456 789", "jordk@gmail.com")
  ];
  contacts.forEach(c => c.render('main'));
  console.log(1)
  