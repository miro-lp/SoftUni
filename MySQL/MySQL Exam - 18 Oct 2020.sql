create schema `softuni_stores_system`;
-- 1.	Table Design
CREATE TABLE `towns` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE `addresses` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    `town_id` INT NOT NULL,
    CONSTRAINT `fk_addresses_towns` FOREIGN KEY (`town_id`)
        REFERENCES `towns` (`id`)
);
    
CREATE TABLE `pictures` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `url` VARCHAR(100) NOT NULL,
    `added_on` DATE NOT NULL
);

CREATE TABLE `categories` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE `stores` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL UNIQUE,
    `rating` FLOAT NOT NULL,
    `has_parking` BOOLEAN DEFAULT FALSE,
    `address_id` INT NOT NULL,
    CONSTRAINT `fk_stores_addresses` FOREIGN KEY (`address_id`)
        REFERENCES `addresses` (`id`)
);

CREATE TABLE `employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(15) NOT NULL,
    `middle_name` CHAR(1),
    `last_name` VARCHAR(20) NOT NULL,
    `salary` DECIMAL(19 , 2 ) DEFAULT 0.00,
    `hire_date` DATETIME NOT NULL,
    `manager_id` INT,
    `store_id` INT NOT NULL,
    CONSTRAINT `fk_employees_employees` FOREIGN KEY (`manager_id`)
        REFERENCES `employees` (`id`),
    CONSTRAINT `fk_employees_stores` FOREIGN KEY (`store_id`)
        REFERENCES `stores` (`id`)
); 

CREATE TABLE `products_stores` (
    `product_id` INT NOT NULL,
    `store_id` INT NOT NULL,
    CONSTRAINT `pk_products_stores` PRIMARY KEY (`product_id` , `store_id`),
    CONSTRAINT `fk_products_stores_stores` FOREIGN KEY (`store_id`)
        REFERENCES `stores` (`id`)
);

CREATE TABLE `products` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(40) NOT NULL UNIQUE,
    `best_before` DATE,
    `price` DECIMAL(10 , 2 ) NOT NULL,
    `description` TEXT,
    `category_id` INT NOT NULL,
    `picture_id` INT NOT NULL,
    CONSTRAINT `fk_products_categories` FOREIGN KEY (`category_id`)
        REFERENCES `categories` (`id`),
    CONSTRAINT `fk_products_pictures` FOREIGN KEY (`picture_id`)
        REFERENCES `pictures` (`id`)
);

alter table `products_stores`
add  CONSTRAINT `fk_products_stores_produts` FOREIGN KEY (`product_id`)
    REFERENCES `products` (`id`);

-- 2.	Insert
insert into `products_stores` (product_id, store_id)
select p.id, 1 from products as p
left join products_stores as ps
on p.id = ps.product_id
where ps.store_id is null;

-- 3.	Update
UPDATE employees AS e
        JOIN
    stores AS s ON e.store_id = s.id 
SET 
    e.manager_id = 3, e.salary = e.salary - 500
WHERE
    DATE_FORMAT(e.hire_date, '%Y') > 2003
        AND s.id != 14
        AND s.id != 5;

-- 04. Delete

delete from employees 
where manager_id is not null and salary>=6000;


-- 5.	Employees 
select first_name, middle_name, last_name, salary, date(hire_date) as 'hire_date' from employees
order by hire_date desc;

-- 6.	Products with old pictures
select p.name as 'product_name', p.price, p.best_before, concat(substring(p.description,1,10),'...') as 'short_description', pc.url
from products as p join pictures as pc
on p.picture_id = pc.id
where char_length(p.description) >100 and date_format(pc.added_on,'%Y') < 2019 and p.price >20
order by p.price desc;

-- 7.	Counts of products in stores and their average 
select s.name, count(p.id) as 'product_count', round(avg(p.price),2) as 'avg' from products as p
join products_stores as ps
on ps.product_id = p.id
right join stores as s
on ps.store_id = s.id
group by s.id
order by product_count desc, avg desc, s.id;

-- 8.	Specific employee
select concat(e.first_name,' ', e.last_name) as 'Full_name', s.name as 'Store_name', a.name, e.salary from employees as e
join stores as s
on e.store_id = s.id
join addresses as a
on s.address_id = a.id
where e.salary < 4000 and a.name like '%5%' and char_length(s.name) > 8 and e.last_name like '%n';

-- 9.	Find all information of stores
select reverse(s.name) as 'reversed_name', concat(upper(t.name),'-',a.name) as 'full_address',
count(e.id) as 'employees_count' from stores as s
join addresses as a
on a.id = s.address_id
join towns as t
on t.id = a.town_id
left join employees as e
on s.id = e.store_id
group by s.id
having employees_count>=1
order by full_address;

-- 10.	Find full name of top paid employee by store name
CREATE FUNCTION `udf_top_paid_employee_by_store` (store_name VARCHAR(50))
RETURNS varchar(100)
deterministic
BEGIN
	
RETURN (select concat(e.first_name,' ', e.middle_name,'. ',e.last_name, ' works in store for ',2020 - year(e.hire_date), ' years')   from employees as e
join stores as s
on s.id = e.store_id
where s.name = store_name
order by e.salary desc
limit 1);
END



-- 11.	Update product price by address
CREATE PROCEDURE `udp_update_product_price`(address_name VARCHAR (50))
BEGIN
update products as p
join products_stores as ps 
on ps.product_id = p.id
join stores as s
on ps.store_id = s.id
join addresses as a
on s.address_id = a.id
set price = (case 
when address_name like '0%' then p.price + 100
else p.price + 200 
end)
where a.name = address_name;
END


