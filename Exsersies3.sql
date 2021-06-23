-- Find Names of All Employees by First Name
select `first_name`, `last_name` from employees
where lower(`first_name`) like 'sa%'
order by `employee_id`;

-- Find Names of All Employees by Last Name
select `first_name`, `last_name` from employees
where lower(`last_name`) like '%ei%'
order by `employee_id`;

-- Find First Names of All Employees
select `first_name` from employees
where `department_id` in (3,10) and year(`hire_date`) between 1995 and 2005
order by `employee_id`;

-- Find All Employees Except Engineers
select `first_name`, `last_name` from employees
where `job_title` not like '%engineer%'
order by `employee_id`;

-- Find Towns with Name Length
select `name` from towns
where char_length(`name`) in (5,6)
order by `name`;

-- Find Towns Starting With
select * from towns
where left(`name`,1) in ('M','K','B','E')
order by `name`;

-- Find Towns Not Starting With
select * from towns
where left(`name`,1) not in ('R','B','D')
order by `name`;

-- Create View Employees Hired After 2000 Year
create view v_employees_hired_after_2000 as
select `first_name`, `last_name` from employees
where year(`hire_date`) > 2000;

select * from v_employees_hired_after_2000;

-- Length of Last Name
select `first_name`, `last_name` from employees
where char_length(`last_name`) = 5;

-- Countries Holding A 3 or More Times
select `country_name`, `iso_code` from countries
where `country_name` like '%a%a%a%'
order by `iso_code`;

-- Mix of Peak and River Names
SELECT 
    `peak_name`,
    `river_name`,
    LOWER(CONCAT(`peak_name`, SUBSTRING(`river_name`, 2))) AS 'mix'
FROM
    peaks,
    rivers
WHERE
    RIGHT(`peak_name`, 1) = LEFT(`river_name`, 1)
ORDER BY `mix`;

-- Games from 2011 and 2012 Year
select `name`, date_format(`start`,'%Y-%m-%d') as 'start' from games
where year(`start`) in (2011,2012)
order by `start`,`name`
limit 50;


-- User Email Providers
select `user_name`, substring(`email`,locate('@',`email`)+1) as 'Email Provider' from users
order by `Email Provider`, `user_name`;

-- Get Users with IP Address Like Pattern
select `user_name`, `ip_address` from users
where `ip_address` like '___.1%.%.___'
order by `user_name`;

-- Show All Games with Duration and Part of the Day
SELECT 
    `name`,
    (CASE
        WHEN HOUR(`start`) BETWEEN 0 AND 11 THEN 'Morning'
        WHEN HOUR(`start`) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END) AS 'Part of the Day',
    (CASE
        WHEN `duration` <= 3 THEN 'Extra Short'
        WHEN `duration` BETWEEN 4 AND 6 THEN 'Short'
        WHEN `duration` BETWEEN 7 AND 10 THEN 'Long'
        ELSE 'Extra Long'
    END) AS 'Duration'
FROM
    games;

-- Orders Table
select `product_name`, `order_date`,
date_add(`order_date`, interval 3 day) as 'pay_due',
date_add(`order_date`, interval 1 month) as 'deliver_due'
 from orders;






