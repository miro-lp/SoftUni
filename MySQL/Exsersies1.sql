CREATE DATABASE `minions`;
USE `minions`;
CREATE TABLE `minions` (
`id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(50) NOT NULL,
`age` INT
);

CREATE TABLE `towns`(
`town_id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(30) NOT NULL
);

ALTER TABLE `minions`
ADD COLUMN `town_id` INT,
ADD CONSTRAINT fk_minions_towns
FOREIGN KEY (`town_id`)
REFERENCES `towns`(`id`);

INSERT INTO `minions`.`towns` (`id`, `name`) 
VALUES 
('1', 'Sofia'),
('2', 'Plovdiv'),
('3', 'Varna');
INSERT INTO `minions` (`id`, `name`, `age`,`town_id`)
VALUES
(1, 'Kevin', 22 , 1),
(2, 'Bob', 15 , 3),
(3, 'Steward', NULL , 2);

TRUNCATE `minions`;

DROP TABLE `minions`;
DROP TABLE `towns`;

CREATE TABLE `people` (
`id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(200) NOT NULL,
`picture` BLOB,
`height` FLOAT(5,2),
`weight` FLOAT(5,2),
`gender` CHAR(1) NOT NULL,
`birthdate` DATE NOT NULL,
`biography` TEXT
);
INSERT INTO `people`
VALUES
(1,'Pesho', NULL, 1.78, 78, 'M', '1984-06-21', NULL),
(2,'Gosho', NULL, 1.88, 80, 'M', '1985-07-26', NULL),
(3,'Ivan', NULL, 1.98, 90, 'M', '1986-08-23', NULL),
(4,'Sofia', NULL, 1.71, 60, 'F', '1987-03-25', NULL),
(5,'Mimi', NULL, 1.65, 50, 'F', '1988-06-20', NULL);

CREATE TABLE `users` (
`id` INT PRIMARY KEY AUTO_INCREMENT,
`username` VARCHAR(30) NOT NULL,
`password` VARCHAR(26) NOT NULL,
`profile_picture` BLOB,
`last_login_time` DATETIME NOT NULL,
`is_deleted` BOOL not null
);

INSERT INTO `users`
VALUES
(1,'Pesho', '12345', NULL, '2021-05-12', 0),
(2,'Gosho', '1fs345', NULL, '2021-05-13', 0),
(3,'Ivan', '123gsv45', NULL, '2021-05-14', 0),
(4,'Sofia', '12sdr345', NULL, '2021-05-15', 0),
(5,'Mimi', '12hj345', NULL, '2021-05-16', 0);

ALTER TABLE `users`
DROP PRIMARY KEY,
ADD CONSTRAINT pk_users
PRIMARY KEY (`id`, `username`);

ALTER TABLE `minions`.`users` 
CHANGE COLUMN `last_login_time` `last_login_time` DATETIME NOT NULL DEFAULT NOW() ;

ALTER TABLE `minions`.`users` 
DROP PRIMARY KEY,
ADD PRIMARY KEY (`id`),
ADD UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE;

create database `Movies`;
use `Movies`;

create table `directors`(
`id` int primary key auto_increment,
`director_name` varchar(30) not null,
`notes` text
);

create table `genres`(
`id` int primary key auto_increment,
`genre_name` varchar(30) not null,
`notes` text
);

create table `categories`(
`id` int primary key auto_increment,
`category_name` varchar(30) not null,
`notes` text
);

create table `movies`(
`id` int primary key auto_increment,
`title` varchar(30) not null,
`director_id` int not null,
`copyright_year` date not null,
`length,` int not null,
`genre_id` int not null,
`category_id` int not null,
`rating` int,
`notes` text,
constraint fk_movies_directors
foreign key (`director_id`) references `directors`(`id`),
constraint fk_movies_genres
foreign key (`genre_id`) references `genres`(`id`),
constraint fk_movies_categories
foreign key (`category_id`) references `categories`(`id`)
);


insert into `directors`
values
(1,'Wachovski',null),
(2,'Ridley Scot',null),
(3,'Lukas',null),
(4,'Tarantino',null),
(5,'Spielbeg',null);

insert into `genres`
values
(1,'Sci Fi',null),
(2,'Thriller',null),
(3,'Drama',null),
(4,'Comedy',null),
(5,'Action',null);

insert into `categories`
values
(1,'Best picture',null),
(2,'Best story',null),
(3,'Best director',null),
(4,'Best screenplay',null),
(5,'Best visual effects',null);

insert into `movies`
values
(1, 'Jupiter ascending', 1, '2016-05-05', 135, 1, 5, 80, null),
(2, 'ET', 5, '1986-07-05', 125, 3, 3, 75, null),
(3, 'Alien', 2, '1992-04-05', 130, 2, 4, 85, null),
(4, 'Star wars', 3, '2006-01-05', 145, 5, 1, 90, null),
(5, 'Django unchained', 4, '2012-07-05', 150, 4, 2, 85, null);

create database `car_rental`;
use `car_rental`;

create table `categories`(
`id` int primary key auto_increment,
`category` varchar(25) not null,
`daily_rate` int,
`weekly_rate` int,
`monthly_rate` int,
`weekend_rate` int
);

create table `cars`(
`id` int primary key auto_increment,
`plate_number` int not null,
`make` varchar(25) not null,
`model` varchar(25) not null,
`car_year` date not null,
`category_id` int not null,
`doors` int not null,
`picture` blob,
`car_condition` text,
`available` boolean not null,
constraint fk_cars_categories
foreign key (`category_id`) references `categories`(`id`)
);

create table `employees`(
`id` int primary key auto_increment,
`first_name` varchar(25) not null,
`last_name` varchar(25) not null,
`title` varchar(25),
`notes` text
);

create table `customers`(
`id` int primary key auto_increment,
`driver_licence_number` int not null,
`full_name` varchar(60) not null,
`address` varchar(50),
`city` varchar(30),
`zip_code` int,
`notes` text
);

create table `rental_orders`(
`id` int primary key auto_increment,
`employee_id` int not null,
`customer_id` int not null,
`car_id` int not null,
`car_condition` text,
`tank_level` decimal(3,1) not null,
`kilometrage_start` int not null,
`kilometrage_end` int not null,
`total_kilometrage` int not null,
`start_date` date not null,
`end_date` date not null,
`total_days` int not null,
`rate_applied` int,
`tax_rate` decimal(5,2),
`order_status` bool not null,
`notes` text,
constraint fk_rental_orders_employees
foreign key (`employee_id`) references `employees`(`id`),
constraint fk_rental_orders_customers
foreign key (`customer_id`) references `customers`(`id`),
constraint fk_rental_orders_cars
foreign key (`car_id`) references `cars`(`id`)
);

insert into `categories`
values
(1,'light', 20, 25, 30, 40),
(2,'heavy', 25, 30, 35, 45),
(3,'small', 10, 15, 20, 40);

insert into `cars`
values
(1,125123, 'fiat', 'punto','2010-01-01',1, 4, null, 'good',1),
(2,125124, 'ford', 'fiesta','2011-01-01',2, 4, null, 'good',0),
(3,125125, 'bmw', '333','2012-01-01',3, 2, null, 'good',1);

insert into `employees`
values
(1,'Pesho','Petrov','Worker',null),
(2,'Pesho','Peshov','D-r',null),
(3,'Ivan','Petrov','Mr',null);

insert into `customers`
values
(1,56789,'Pesho Petrov','Sofia','Sofia',1000, null),
(2,44789,'Ivan Petrov','Sofia','Sofia',1000, null),
(3,88789,'Kiko Petrov','Sofia','Sofia',1000, null);

insert into `rental_orders`
values
(1,1,1,1,'good',0.5,120000,125000,5000, '2020-10-10','2020-10-20',10,20,5.2,1,null),
(2,3,2,3,'good',0.6,121000,124000,3000, '2020-11-15','2020-11-20',5,25,5.5,0,null),
(3,2,3,2,'good',0.5,122000,126000,4000, '2020-10-05','2020-10-15',10,15,3.2,1,null);

create database `soft_uni`;
use `soft_uni`;
create table `towns`(
`id` int primary key auto_increment,
`name` varchar(30) not null
);

create table `addresses`(
`id` int primary key auto_increment,
`address_text` varchar(120) not null,
`town_id` int not null,
constraint fk_addresses_towns
foreign key (`town_id`) references `towns`(`id`)
);

create table `departments`(
`id` int primary key auto_increment,
`name` varchar(30) not null
);

create table `employees`(
`id` int primary key auto_increment,
`first_name` varchar(30) not null,
`middle_name` varchar(30) not null,
`last_name` varchar(30) not null,
`job_title` varchar(25),
`department_id` int,
`hire_date` date,
`salary` decimal(10,2),
`address_id` int,
constraint fk_employess_departments
foreign key (`department_id`) references `departments`(`id`),
constraint fk_employess_addresses
foreign key (`address_id`) references `addresses`(`id`)
);

insert into `towns` (`name`)
value
('Sofia'),
('Plovdiv'),
('Varna'),
('Burgas');

insert into `departments` (`name`)
value
('Engineering'),
('Sales'),
('Marketing'),
('Software Development'),
('Quality Assurance');

insert into `employees` (`id`, `first_name`, `middle_name`,
`last_name`, `job_title`, `department_id`, `hire_date`, `salary` )
value
(1, 'Ivan', 'Ivanov', 'Ivanov', '.NET Developer', 4, '2013-02-01', 3500),
(2, 'Petar', 'Petrov', 'Petrov', 'Senior Engineer', 1, '2004-03-02', 4000),
(3, 'Maria', 'Petrova', 'Ivanova', 'Intern', 5, '2016-08-28', 525.25),
(4, 'Georgi', 'Terziev', 'Ivanov', 'CEO', 2, '2007-12-09', 3000),
(5, 'Peter', 'Pan', 'Pan', 'Intern', 3, '2016-08-28', 599.88);

select * from `towns`;
select * from `departments`;
select * from `employees`;

select `name` from `towns`
order by `name`;

select `name` from `departments`
order by `name`;

select `first_name`, `last_name`,`job_title`,`salary` from `employees`
order by `salary` desc;

update `employees`
set `salary` = `salary`* 1.1;

select `salary` from `employees`;

truncate `employees`;




