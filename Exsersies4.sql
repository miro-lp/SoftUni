-- Records' Count
select  count(*) as 'count' from wizzard_deposits;

-- Longest Magic Wand
select max(`magic_wand_size`) as 'longest_magic_wand' from wizzard_deposits;

-- Longest Magic Wand Per Deposit Groups
select `deposit_group`, max(`magic_wand_size`) as 'longest_magic_wand'
from wizzard_deposits
group by `deposit_group`
order by `longest_magic_wand`, `deposit_group`;

-- Smallest Deposit Group Per Magic Wand Size*
select `deposit_group`
from wizzard_deposits
group by `deposit_group`
having avg(`magic_wand_size`)
limit 1;

-- Deposits Sum
select `deposit_group`, sum(`deposit_amount`) as 'total_sum'
from wizzard_deposits
group by `deposit_group`
order by `total_sum`;

-- Deposits Sum for Ollivander Family
select `deposit_group`, sum(`deposit_amount`) as 'total_sum'
from wizzard_deposits
where `magic_wand_creator` = 'Ollivander family'
group by `deposit_group`
order by `deposit_group`;

-- Deposits Filter
select `deposit_group`, sum(`deposit_amount`) as 'total_sum'
from wizzard_deposits
where `magic_wand_creator` = 'Ollivander family'
group by `deposit_group`
having `total_sum`<150000
order by `total_sum` desc;

-- Deposit Charge
select `deposit_group`, `magic_wand_creator`, min(`deposit_charge`) as `min_deposit_charge`
from wizzard_deposits
group by `deposit_group`, `magic_wand_creator`
order by `magic_wand_creator`, `deposit_group`;

-- Age Groups
select (case
		when `age` between 0 and 10 then '[0-10]'
        when `age` between 11 and 20 then '[11-20]'
        when `age` between 21 and 30 then '[21-30]'
        when `age` between 31 and 40 then '[31-40]'
        when `age` between 41 and 50 then '[41-50]'
		when `age` between 51 and 60 then '[51-60]'      
		when `age`>60 then '[61+]' 
end
) as 'age_group', count(*) as 'wizard_count'
from wizzard_deposits
group by age_group
order by age_group;

-- First Letter
select left(first_name,1) as 'first_letter' from wizzard_deposits
where `deposit_group` = 'Troll Chest'
group by first_letter
order by first_letter;

-- Average Interest 
select `deposit_group`, `is_deposit_expired`, avg(`deposit_interest`) as 'average_interest'
from wizzard_deposits
where `deposit_start_date` > '1985-01-01'
group by `deposit_group`, `is_deposit_expired`
order by `deposit_group` desc, `is_deposit_expired`;

-- Employees Minimum Salaries
select `department_id`, min(`salary`) as 'minimum_salary'
from employees
where `department_id` in (2,5,7) and `hire_date` > '2000-01-01 00:00:00.000000'
group by `department_id`
order by `department_id`;

--  Employees Average Salaries
create table `employees_new` 
select * from employees 
where salary >30000 and manager_id != 42;

update `employees_new`
set `salary` = `salary` + 5000
where `department_id` = 1;

select `department_id`, avg(`salary`) as avg_salary
from `employees_new`
group by `department_id`
order by `department_id`;

-- Employees Maximum Salaries
select `department_id`, max(`salary`) as max_salary
from employees
group by `department_id`
having max_salary>70000 or max_salary <30000
order by `department_id`;

-- Employees Count Salaries
select count(salary) as '' from employees
where manager_id is null
group by manager_id;

-- 3rd Highest Salary*
select e.department_id, ( 
	select distinct e2.salary from employees as e2
	where e2.department_id = e.department_id
	order by e2.salary desc
	limit 1 offset 2
) as 'third_highest_salary' 
from employees as e
group by e.department_id
having third_highest_salary is not null
order by e.department_id;

--  Salary Challenge**
select e.first_name, e.last_name, e.department_id
from employees as e
where salary >(select avg(e2.salary) from employees as e2
where e2.department_id = e.department_id)
order by department_id, employee_id
limit 10;

-- Departments Total Salaries
select department_id, sum(salary) as 'total_salary'
from employees
group by department_id
order by department_id;

