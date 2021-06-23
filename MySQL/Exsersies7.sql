

-- Employees with Salary Above 35000
CREATE  PROCEDURE `usp_get_employees_salary_above_35000`()
BEGIN
	select first_name, last_name from employees
	where salary >35000
	order by first_name, last_name, employee_id;
END

-- Employees with Salary Above Number
CREATE  PROCEDURE `usp_get_employees_salary_above`(salary_search decimal(10,4))
BEGIN
	select first_name, last_name from employees
	where salary >= salary_search
	order by first_name, last_name, employee_id;
END


-- Town Names Starting With
CREATE  PROCEDURE `usp_get_towns_starting_with`(letter varchar(10))
BEGIN
	select `name` as 'town_name' from towns
	where `name` like concat(letter,'%')
	order by `name`;
END

-- Employees from Town
CREATE PROCEDURE `usp_get_employees_from_town` (town_name varchar(25))
BEGIN
	select first_name, last_name from employees
	join addresses
	using (address_id)
	join towns
	using (town_id)
	where `name` = town_name
	order by first_name, last_name, employee_id;
END

-- Salary Level Function
CREATE FUNCTION `ufn_get_salary_level`(salary decimal(12,4)) RETURNS varchar(25) CHARSET utf8
    DETERMINISTIC
BEGIN

	
RETURN (case
		when salary < 30000 then 'Low'
		when salary > 50000 then 'High'
		else 'Average'
		end);
END

-- Employees by Salary Level
CREATE  PROCEDURE `usp_get_employees_by_salary_level`(type_salary varchar(15))
BEGIN
	select first_name, last_name from employees
	where (case
		when salary < 30000 then 'Low'
		when salary > 50000 then 'High'
		else 'Average'
		end) = type_salary
	order by first_name desc, last_name desc;

END

-- Define Function
CREATE FUNCTION `ufn_is_word_comprised` (set_of_letters varchar(50), word varchar(50))
RETURNS INTEGER
deterministic
BEGIN

RETURN (select word regexp(concat('^[',set_of_letters,']+$')));
END

-- Find Full Name
CREATE PROCEDURE `usp_get_holders_full_name` ()
BEGIN
	select concat(`first_name`,' ',`last_name`) as 'full_name' from account_holders
	order by full_name;
END

-- People with Balance Higher Than
CREATE PROCEDURE `usp_get_holders_with_balance_higher_than`(salary decimal(12,2))
BEGIN
	select ah.first_name, ah.last_name from account_holders as ah
	join accounts as a 
	on a.account_holder_id = ah.id
	group by ah.id 
	having sum(a.balance) > salary
	order by ah.id;
END

-- Future Value Function
CREATE FUNCTION `ufn_calculate_future_value` (initial_sum decimal(14,4), interest_rate decimal(10,4), year_num int)
RETURNS decimal (18,4)
deterministic
BEGIN
declare calculare_values decimal (18,4);
set calculare_values:= pow((1+interest_rate),year_num)*initial_sum;

RETURN calculare_values;
END

-- Calculating Interest
CREATE  PROCEDURE `usp_calculate_future_value_for_account`(account_id int, interest_rate decimal(10,4))
BEGIN
	select ah.id as 'account_id', ah.first_name, ah.last_name, a.balance as 'current_balance', 
	ufn_calculate_future_value(a.balance, interest_rate, 5) as 'balance_in_5_years' from account_holders as ah
	join accounts as a 
	on a.account_holder_id = ah.id
	where a.id = account_id;
END

-- Deposit Money
CREATE PROCEDURE `usp_deposit_money` (account_id int , money_amount decimal (19,4))
BEGIN
	if money_amount > 0 then start transaction;
    
		update accounts as a set balance = balance + money_amount 
        where a.id = account_id;
        commit;
	else rollback;
    end if;

END

-- Withdraw Money
CREATE PROCEDURE `usp_withdraw_money` (account_id int, money_amount decimal(18,4))
BEGIN
	if money_amount > 0 then start transaction;
    
		update accounts as a set balance = balance - money_amount 
        where a.id = account_id;
        if (select balance from accounts where id = account_id) < 0 then rollback;
        else commit;
        end if;
	else rollback;
	end if;
END

-- Money Transfer

CREATE PROCEDURE `usp_transfer_money` (from_account_id int, to_account_id int, amount decimal(19,4))
BEGIN
	if amount >0 and (select id from accounts where id = from_account_id ) is not null and
    (select id from accounts where id = to_account_id ) is not null 
    then start transaction;
		update accounts set balance = balance - amount
        where id = from_account_id;
        update accounts set balance = balance + amount
        where id = to_account_id;
        if (select balance from accounts where id =from_account_id ) <0 then rollback;
        else commit;
        end if;
    
    else rollback;
    end if;

END

-- Log Accounts Trigger
CREATE TABLE `logs` (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    old_sum DECIMAL(18 , 4 ),
    new_sum DECIMAL(18 , 4 )
);
 
 create trigger `tr_accounts_changes` 
 after update on accounts
 for each row
 begin
	insert into `logs` (account_id, old_sum, new_sum)
    values (old.id, old.balance, new.balance);
 end

-- Emails Trigger
CREATE TABLE `notification_emails` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    recipient INT,
    `subject` VARCHAR(60),
    body TEXT
);
 
 create trigger `tr_mail_accounts_changes` 
 after insert on `logs`
 for each row
 begin
	insert into `notification_emails` (recipient, subject, body)
    values (new.account_id, concat('Balance change for account: ', new.account_id), concat('On ',date_format(current_timestamp(),'%b %d %Y'),
    ' at ', date_format(current_timestamp(),'%r'), ' your balance was hanged from ',format(new.old_sum,0), ' to ', format(new.new_sum,0),'.'));
 end

