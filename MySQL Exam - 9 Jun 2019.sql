create schema `ruk_database`;
use ruk_database;
-- 01.	Table Design

CREATE TABLE `clients` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `full_name` VARCHAR(50) NOT NULL,
    `age` INT NOT NULL
);

CREATE TABLE `bank_accounts` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `account_number` VARCHAR(10) NOT NULL,
    `balance` DECIMAL(10 , 2 ) NOT NULL,
    `client_id` INT NOT NULL UNIQUE,
    CONSTRAINT `fk_bank_accounts_clients` FOREIGN KEY (`client_id`)
        REFERENCES `clients` (`id`)
);

CREATE TABLE `cards` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `card_number` VARCHAR(19) NOT NULL,
    `card_status` VARCHAR(7) NOT NULL,
    `bank_account_id` INT NOT NULL,
    CONSTRAINT `fk_cards_bank_accounts` FOREIGN KEY (`bank_account_id`)
        REFERENCES `bank_accounts` (`id`)
);

CREATE TABLE `branches` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE `employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(20) NOT NULL,
    `last_name` VARCHAR(20) NOT NULL,
    `salary` DECIMAL(10 , 2 ) NOT NULL,
    `started_on` DATE NOT NULL,
    `branch_id` INT NOT NULL,
    CONSTRAINT `fk_employees_branches` FOREIGN KEY (`branch_id`)
        REFERENCES `branches` (`id`)
);

CREATE TABLE `employees_clients` (
    `employee_id` INT,
    `client_id` INT,
    CONSTRAINT `fk_employees_clients_employees` FOREIGN KEY (`employee_id`)
        REFERENCES `employees` (`id`),
    CONSTRAINT `fk_employees_clients_clients` FOREIGN KEY (`client_id`)
        REFERENCES `clients` (`id`)
);

-- 02.	Insert

insert into cards (card_number, card_status, bank_account_id)
select reverse(full_name), 'Active', id from clients where id between 191 and 200;

-- 03.	Update
update employees_clients as ac_1
join (select ec.employee_id from employees_clients as ec
group by ec.employee_id
order by count(ec.client_id), ec.employee_id
limit 1) as s
set ac_1.employee_id =s.employee_id
where ac_1.employee_id = ac_1.client_id;

-- 04.	Delete
delete from employees
where id not in (select employee_id from employees_clients);

-- 05.	Clients

select id, full_name from clients
order by id;

-- 06.	Newbies

select id, concat(first_name,' ', last_name) as 'full_name', concat('$',salary) as 'salary', started_on from employees
where salary >= 100000 and started_on >= '2018-01-01'
order by salary desc, id;

-- 07.	Cards against Humanity

select c.id, concat(c.card_number,' : ', cl.full_name) as card_token from cards as c
join bank_accounts as ba
on c.bank_account_id = ba.id
join clients as cl
on ba.client_id = cl.id
order by c.id desc;

-- 08.	Top 5 Employees
select concat(e.first_name,' ',e.last_name) as 'name', e.started_on, count(ec.client_id) as 'count_of_clients' from employees as e
join employees_clients as ec
on e.id = ec.employee_id
group by ec.employee_id
order by count_of_clients desc, e.id
limit 5;

-- 09.	Branch cards
select b.name, count(c.id) as 'count_of_cards' from branches as b
left join employees as e
on e.branch_id = b.id
left join employees_clients as ec
on e.id = ec.employee_id
left join clients as cl
on cl.id = ec.client_id
left join bank_accounts as ba
on ba.client_id = cl.id
left join cards as c
on c.bank_account_id = ba.id
group by b.id
order by count_of_cards desc, b.name;

-- 10.	Extract client cards count