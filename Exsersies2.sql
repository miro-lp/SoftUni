-- Find All Information About Departments
SELECT * FROM `departments`
order by `department_id`;

-- Find all Department Names
select `name` from departments
order by `department_id`;

-- Find all Department Names
select `first_name`, `last_name`, `salary` from employees
order by `employee_id`;

-- Find Full Name of Each Employee
select `first_name`, `middle_name`, `last_name` from employees
order by `employee_id`;

-- Find Email Address of Each Employee
select concat(`first_name`,'.',`last_name`,'@softuni.bg')
as 'full_email_address' from employees;

-- Find All Different Employee's Salaries
select distinct `salary` from employees;

-- Find all Information About Employees
select * from `employees`
where `job_title`='Sales Representative';

-- Find Names of All Employees by salary in Range
select `first_name`, `last_name`, `job_title` from `employees`
where `salary`>=20000 and `salary`<=30000;

-- Find Names of All Employees
select concat_ws(' ',`first_name`, `middle_name`, `last_name`) from employees
as `Full Name`
where `salary` in (25000, 14000, 12500, 23600);

-- Find All Employees Without Manager
select `first_name`, `last_name` from `employees`
where `manager_id` is null;

-- Find All Employees with salary More Than 50000
select `first_name`, `last_name`, `salary` from `employees`
where `salary`>50000
order by `salary` desc;

-- Find 5 Best Paid Employees
select  `first_name`, `last_name` from `employees`
order by `salary` desc limit 5;

-- Find All Employees Except Marketing
select  `first_name`, `last_name` from `employees`
where `department_id`!=4;

-- Sort Employees Table
select * from `employees`
order by `salary`desc,`first_name`,`last_name` desc, `middle_name`;

-- Create View Employees with Salaries
create view `v_employees_salaries` as
select `first_name`, `last_name`, `salary` from `employees`;

-- Create View Employees with Job Titles
create view v_employees_job_titles as
select concat_ws(' ',`first_name`, `middle_name`, `last_name`)
as `full_name` , `job_title`  from `employees`;

-- Distinct Job Titles
select distinct `job_title`  from `employees`
order by `job_title`;

-- Find First 10 Started Projects
select * from `projects`
order by `start_date`, `name`, `project_id` limit 10;

-- Last 7 Hired Employees
select `first_name`, `last_name`, `hire_date` from `employees`
order by `hire_date` desc
limit 7 ;

-- Increase Salaries
update `employees`
set `salary` = `salary`*1.12
where `department_id` in (1,2,4,11);
select `salary` from `employees`;

-- All Mountain Peaks 
select `peak_name` from `peaks`
order by `peak_name`;

-- Biggest Countries by Population
select `country_name`, `population` from `countries`
where `continent_code` = 'EU'
order by `population` desc,  `country_name`
limit 30;

-- Countries and Currency (Euro / Not Euro)
select `country_name`, `country_code`, if(`currency_code`='EUR','Euro','Not Euro' ) 
as 'currency' 
from `countries`
order by `country_name`;

-- All Diablo Characters
SELECT `name` FROM `characters`
order by `name`;

