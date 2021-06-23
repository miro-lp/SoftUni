create schema `stc`;
use `stc`;

-- 1.	Table Design
CREATE TABLE `addresses` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL);

CREATE TABLE `clients` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `full_name` VARCHAR(50) NOT NULL,
    `phone_number` VARCHAR(20) NOT NULL
);

CREATE TABLE `drivers` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(30) NOT NULL,
    `last_name` VARCHAR(30) NOT NULL,
    `age` INT NOT NULL,
    `rating` FLOAT DEFAULT 5.5
);

CREATE TABLE `categories` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10) NOT NULL
    );

CREATE TABLE `cars` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `make` VARCHAR(20) NOT NULL,
    `model` VARCHAR(20),
    `year` INT NOT NULL DEFAULT 0,
    `mileage` INT DEFAULT 0,
    `condition` CHAR(1) NOT NULL,
    `category_id` INT NOT NULL,
    CONSTRAINT fk_cars_categories FOREIGN KEY (`category_id`)
        REFERENCES `categories` (`id`)
);

CREATE TABLE `cars_drivers` (
    `car_id` INT NOT NULL,
    `driver_id` INT NOT NULL,
    CONSTRAINT `pk_cars_drivers` PRIMARY KEY (`car_id` , `driver_id`),
    CONSTRAINT `fk_cars_drivers_cars` FOREIGN KEY (`car_id`)
        REFERENCES `cars` (`id`),
    CONSTRAINT `fk_cars_drivers_drivers` FOREIGN KEY (`driver_id`)
        REFERENCES `drivers` (`id`)
);


CREATE TABLE `courses` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `from_address_id` INT NOT NULL,
    `start` DATETIME NOT NULL,
    `bill` DECIMAL(10 , 2 ) DEFAULT 10.00,
    `car_id` INT NOT NULL,
    `client_id` INT NOT NULL,
    CONSTRAINT `fk_courses_addresses` FOREIGN KEY (`from_address_id`)
        REFERENCES `addresses` (`id`),
    CONSTRAINT `fk_courses_cars` FOREIGN KEY (`car_id`)
        REFERENCES `cars` (`id`),
    CONSTRAINT `fk_courses_clients` FOREIGN KEY (`client_id`)
        REFERENCES `clients` (`id`)
);


-- 2.	Insert

insert into clients (full_name, phone_number)
select concat(first_name,' ', last_name), concat('(088) 9999',id*2) from drivers
where id between 10 and 20;

-- 3.	Update

update cars
set `condition` = 'C'
where mileage>=400000 or mileage is null and make !='Mercedes-Benz' and year<= '2010';


-- 4.	Delete

delete cl  from clients as cl
left join courses as c
on cl.id = c.client_id
where char_length(cl.full_name) >3 and c.id is null;

-- 5.	Cars

select make, model, `condition` from cars
order by id;

-- 6.	Drivers and Cars
select d.first_name, d.last_name, c.make, c.model, c.mileage from drivers as d
join cars_drivers as cd
on cd.driver_id = d.id
join cars as c
on cd.car_id = c.id
where c.mileage is not null
order by c.mileage desc, d.first_name;


-- 7.	Number of courses for each car
select c.id as 'car_id', c.make, c.mileage, count(cr.id) as 'count_of_courses', round(avg(cr.bill),2) as 'avg_bill' from cars as c
left join courses as cr
on c.id = cr.car_id
group by c.id
having count_of_courses!=2
order by count_of_courses desc, c.id;

-- 8.	Regular clients

select cl.full_name, count(c.id) as 'count_of_cars', sum(cr.bill) as 'total_sum' from clients as cl
left join courses as cr
on cl.id = cr.client_id
join cars as c
on c.id = cr.car_id
where cl.full_name like '_a%'
group by cl.id
having count_of_cars >1
order by full_name
;

-- 9.	Full information of courses
select a.name, (case 
when date_format(cr.start,'%T') between '06:00:00' and '20:59:59' then 'Day'
else 'Night'
end) as 'day_time', cr.bill, cl.full_name, c.make, c.model, ct.name as 'category_name' from courses as cr
left join addresses as a
on a.id = cr.from_address_id
left join cars as c
on c.id = cr.car_id
left join clients as cl
on cl.id = cr.client_id
left join categories as ct
on ct.id = c.category_id
order by cr.id;

select count(cr.id) from clients as cl
join courses as cr
on cl.id = cr.client_id
where cl.phone_number = '(803) 6386812'
group by cl.id;

-- 10.	Find all courses by client’s phone number
CREATE FUNCTION `udf_courses_by_client` (phone_num VARCHAR (20))
RETURNS INTEGER
BEGIN

RETURN (select count(cr.id) from clients as cl
join courses as cr
on cl.id = cr.client_id
where cl.phone_number = phone_num
group by cl.id);
END

-- 11.	Full info for address

CREATE PROCEDURE `udp_courses_by_address` (address_name varchar(100) )
BEGIN
	select  a.name, cl.full_name, (case 
	when cr.bill <=20 then 'Low'
	when cr.bill>30 then 'High'
	else 'Medium'
	 end) as 'level_of_bill' , c.make, c.`condition`, ct.name as 'cat_name' from addresses as a
	left join courses as cr
	on a.id = cr.from_address_id
	left join cars as c
	on c.id = cr.car_id
	left join clients as cl
	on cl.id = cr.client_id
	left join categories as ct
	on ct.id = c.category_id
	where a.name = address_name
	order by c.make, cl.full_name;

END
