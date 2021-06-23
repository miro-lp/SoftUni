create schema `exsersies5`;
-- One-To-One Relationship
create table `passports` (
`passport_id` int primary key auto_increment,
`passport_number` varchar(25) unique
);
alter table passports auto_increment = 101;

create table `people` (
`person_id` int primary key auto_increment,
`first_name` varchar(25),
`salary` decimal(10,2),
`passport_id` int unique,
constraint fk_people_passports
foreign key (`passport_id`) references `passports`(`passport_id`)
);


insert into passports values
(101, 'N34FG21B'),
(102, 'K65LO4R7'),
(103, 'ZE657QP2');

insert into people values
(1, 'Roberto', 43300, 102),
(2, 'Tom', 56100, 103),
(3, 'Yana', 60200, 101);

-- One-To-Many Relationship

create table `manufacturers` (
`manufacturer_id` int primary key auto_increment,
`name` varchar(25),
`established_on` date
);

create table `models` (
`model_id` int primary key unique,
`name` varchar(25),
`manufacturer_id` int,
constraint fk_models_manufacturers
foreign key (`manufacturer_id`) references `manufacturers`(`manufacturer_id`)
);

alter table `models` auto_increment = 101;

insert into `manufacturers` values
(1, 'BMW', '1916-03-01'),
(2, 'Tesla', '2003-01-01'),
(3, 'Lada', '1966-05-01');

insert into `models` values
(101, 'X1', 1),
(102, 'i6', 1),
(103, 'Model S', 2),
(104, 'Model X', 2),
(105, 'Model 3', 2),
(106, 'Nova', 3);

-- Many-To-Many Relationship
create table `students` (
`student_id` int primary key auto_increment,
`name` varchar(20)
);

create table `exams` (
`exam_id` int primary key auto_increment,
`name` varchar(20)
);

create table `students_exams` (
`student_id` int,
`exam_id` int,
constraint pk_students_exams
primary key(`student_id`,`exam_id`),
constraint fk_students_exams_students
foreign key (`student_id`) references `students`(`student_id`),
constraint fk_students_exams_exams
foreign key (`exam_id`) references `exams`(`exam_id`)
);

insert into students value
(1,'Mila'),
(2,'Toni'),
(3,'Ron');

insert into exams value
(101,'Spring MVC'),
(102,'Neo4j'),
(103,'Oracle 11g');

insert into students_exams value
(1,101),
(1,102),
(2,101),
(3,103),
(2,102),
(2,103);

-- Self-Referencing
create table `teachers` (
`teacher_id` int primary key auto_increment,
`name` varchar(20),
`manager_id` int,
constraint fk_teacher_id_manager_id
foreign key (`manager_id`) references `teachers`(`teacher_id`)
);


insert into teachers (`teacher_id`, `name`) values 
(101, 'John'),
(102, 'Maya'),
(103, 'Silvia'),
(104, 'Ted'),
(105, 'Mark'),
(106, 'Greta');

update teachers 
set `manager_id` = 106
where `teacher_id` in (102,103);

update teachers 
set `manager_id` = 101
where `teacher_id` in (105,106);

update teachers 
set `manager_id` = 105
where `teacher_id` in (104);

-- Online Store Database
create table `cities`(
`city_id` int primary key auto_increment,
`name` varchar(50)
);

create table `item_types`(
`item_type_id` int primary key auto_increment,
`name` varchar(50)
);

create table `customers` (
`customer_id` int primary key auto_increment,
`name` varchar(50),
`birthday` date,
`city_id` int,
constraint fk_customers_cities
foreign key (`city_id`) references `cities`(`city_id`)
);

create table `orders` (
`order_id` int primary key auto_increment,
`customer_id` int,
constraint fk_orders_customers
foreign key (`customer_id`) references `customers`(`customer_id`)
);

create table `items` (
`item_id` int primary key auto_increment,
`name` varchar(50),
`item_type_id` int,
constraint fk_items_item_types
foreign key (`item_type_id`) references `item_types`(`item_type_id`)
);

create table order_items (
`order_id` int,
`item_id` int,
constraint pk_order_item
primary key(`order_id`,`item_id`),
constraint fk_order_itmes_orders
foreign key (`order_id`) references `orders`(`order_id`),
constraint fk_order_itmes_items
foreign key (`item_id`) references `items`(`item_id`)
);

-- University Database
create table `subjects`(
`subject_id` int primary key auto_increment,
`subject_name` varchar(50)
);

create table `majors`(
`major_id` int primary key auto_increment,
`name` varchar(50)
);

create table `students`(
`student_id` int primary key auto_increment,
`student_number` varchar(12),
`student_name` varchar(50),
`major_id` int,
constraint fk_students_majors
foreign key (`major_id`) references `majors`(`major_id`)
);

create table `payments`(
`payment_id` int primary key auto_increment,
`payment_date` date,
`payment_amount` decimal(8,2),
`student_id` int,
constraint fk_payments_students
foreign key (`student_id`) references `students`(`student_id`)
);

create table `agenda` (
`student_id` int,
`subject_id` int,
constraint pk_student_subject
primary key(`student_id`,`subject_id`),
constraint fk_agenda_students
foreign key (`student_id`) references `students`(`student_id`),
constraint fk_agenda_subject
foreign key (`subject_id`) references `subjects`(`subject_id`)
);


-- Peaks in Rila

select mountain_range, peak_name, elevation from mountains
join peaks
on mountains.id = peaks.mountain_id
where mountain_range = 'Rila'
order by elevation desc;