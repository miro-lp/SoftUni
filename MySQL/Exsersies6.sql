-- Employee Address
select employee_id, job_title, address_id, address_text from employees
join addresses 
using (address_id)
order by address_id
limit 5;

-- Addresses with Towns
select first_name, last_name, `name` as 'town', address_text from employees
join addresses
using (address_id)
join towns
using (town_id)
order by first_name, last_name
limit 5;

-- Sales Employee
select employee_id, first_name, last_name, `name` as 'department_name' from employees
join departments
using (department_id)
where `name`= 'Sales'
order by employee_id desc;

-- Employee Departments
select employee_id, first_name, salary, `name` as department_name from employees
join departments
using (department_id)
where salary > 15000
order by department_id desc, first_name
limit 5;

-- Employees Without Project
select employee_id, first_name from employees
left join employees_projects
using (employee_id)
where project_id is null
order by employee_id desc
limit 3;

-- Employees Hired After
select first_name, last_name, hire_date, `name` as dept_name from employees
join departments
using (department_id)
where hire_date > '199-01-01' and name = 'Sales' or name = 'Finance'
order by hire_date;

--  Employees with Project
select employee_id, first_name, name as project_name from employees
join employees_projects using (employee_id)
join projects using (project_id)
where date(start_date) > '2002-08-13' and end_date is null
order by first_name, `name`
limit 5;

-- Employee 24
select employee_id, first_name,
 (case
when year(start_date) > 2004 then null
else `name`
end) as project_name from employees
join employees_projects using (employee_id)
join projects using (project_id)
where employee_id = 24
order by `name`;

-- Employee Manager
select e1.employee_id, e1.first_name, e1.manager_id, e2.first_name as 'manager_name' from employees as e1
join employees as e2
on  e1.manager_id=e2.employee_id 
where e1.manager_id in (3,7)
order by e1.first_name;

-- Employee Summary
select e1.employee_id, concat(e1.first_name,' ', e1.last_name) as 'employee_name', concat(e2.first_name,' ', e2.last_name) as 'manager_name',
d.name as 'department_name' from employees as e1
join employees as e2
on  e1.manager_id=e2.employee_id
join departments as d
on  e1.department_id=d.department_id
order by e1.employee_id
limit 5;

-- Min Average Salary
select avg(salary) as 'min_average_salary' from employees
group by department_id
order by min_average_salary 
limit 1;

-- Highest Peaks in Bulgaria
select c.country_code, m.mountain_range, p.peak_name, p.elevation from countries as c
join mountains_countries as mc
on mc.country_code = c.country_code 
join mountains as m
on m.id = mc.mountain_id
join peaks as p
on m.id = p.mountain_id
where c.country_code = 'BG' and p.elevation>2835
order by p.elevation desc;

-- Count Mountain Ranges
select c.country_code, count(m.mountain_range) as 'mountain_range' from countries as c
join mountains_countries as mc
on mc.country_code = c.country_code 
join mountains as m
on m.id = mc.mountain_id
where c.country_code in ('BG','RU','US')
group by c.country_code
order by mountain_range desc;

-- Countries with Rivers
select country_name, river_name from countries as c
left join countries_rivers as cr
on c.country_code = cr.country_code 
left join rivers as r
on cr.river_id = r.id
where continent_code = "AF"
order by country_name
limit 5;

-- Continents and Currencies
select c1.continent_code, c1.currency_code, count(c2.currency_code) as  'currency_usage' from countries as c1
join countries as c2
using (country_name)
where c1.currency_code = c2.currency_code
group by c1.continent_code, c1.currency_code
having (select )
order by continent_code, currency_code;

-- Countries Without Any Mountains
select count(*) from countries
left join mountains_countries
using (country_code)
where mountain_id is null;

--  Highest Peak and Longest River by Country
select c.country_name,max(p.elevation) as 'highest_peak_elevation', max(r.length) as 'longest_river_length' from countries as c
join countries_rivers as cr
on cr.country_code=c.country_code
join rivers as r
on r.id=cr.river_id
join mountains_countries as mc
on mc.country_code=c.country_code
join mountains as m
on mc.mountain_id = m.id
join peaks as p
on p.mountain_id = m.id
group by c.country_name
order by highest_peak_elevation desc,longest_river_length desc, c.country_name
limit 5;

