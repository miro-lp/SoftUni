create schema `fsd`;
-- 1.	Table Design
CREATE TABLE `coaches` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(10) NOT NULL,
    `last_name` VARCHAR(20) NOT NULL,
    `salary` DECIMAL(10 , 2 ) NOT NULL DEFAULT 0.00,
    `coach_level` INT NOT NULL DEFAULT 0
);
CREATE TABLE `players_coaches` (
    `player_id` INT,
    `coach_id` INT,
    CONSTRAINT `fk_players_coaches_coaches` 
    FOREIGN KEY (`coach_id`) REFERENCES `coaches` (`id`)
);

CREATE TABLE `skills_data` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `dribbling` INT DEFAULT 0,
    `pace` INT DEFAULT 0,
    `passing` INT DEFAULT 0,
    `shooting` INT DEFAULT 0,
    `speed` INT DEFAULT 0,
    `strength` INT DEFAULT 0
    );
    
CREATE TABLE `countries` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL
);
    
  CREATE TABLE `towns` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,
    `country_id` INT not null,
    CONSTRAINT `fk_towns_countries` 
    FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
);

  CREATE TABLE `stadiums` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,
    `capacity` INT not null,
    `town_id` INT not null,
    CONSTRAINT `fk_stadiums_towns` 
    FOREIGN KEY (`town_id`) REFERENCES `towns` (`id`)
);

CREATE TABLE `teams` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,
    `established` DATE NOT NULL,
    `fan_base` BIGINT NOT NULL,
    `stadium_id` INT NOT NULL,
    CONSTRAINT `fk_teams_stadiums` FOREIGN KEY (`stadium_id`)
        REFERENCES `stadiums` (`id`)
);
CREATE TABLE `players` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(10) NOT NULL,
    `last_name` VARCHAR(20) NOT NULL,
    `age` INT NOT NULL DEFAULT 0,
    `position` CHAR(1) NOT NULL,
    `salary` DECIMAL(10 , 2 ) NOT NULL DEFAULT 0.00,
    `hire_date` DATETIME,
    `skills_data_id` INT NOT NULL,
    `team_id` INT,
    CONSTRAINT `fk_skills_data_players` FOREIGN KEY (`skills_data_id`)
        REFERENCES `skills_data` (`id`),
    CONSTRAINT `fk_teams_players` FOREIGN KEY (`team_id`)
        REFERENCES `teams` (`id`)
); 
alter table `players_coaches`
add  CONSTRAINT `fk_players_coaches_players` FOREIGN KEY (`player_id`)
    REFERENCES `players` (`id`);

-- 2.	Insert
insert into `coaches`(first_name, last_name, salary, coach_level)
select first_name, last_name, salary*2, char_length(first_name) from players where age >=45;

-- 3.	Update
update `coaches`
set coach_level = coach_level + 1 
where first_name like 'A%' and id in (select coach_id from players_coaches where player_id is not null);

-- 4.	Delete

delete from players
where age >=45;

-- 5.	Players
select first_name, age, salary from players
order by salary desc;

-- 6.	Young offense players without contract
SELECT 
    p.id,
    CONCAT(p.first_name, ' ', p.last_name) AS 'full_name',
    p.age,
    p.position,
    p.hire_date
FROM
    players AS p
        JOIN
    skills_data AS sk ON p.skills_data_id = sk.id
WHERE
    p.age < 23 AND p.position = 'A'
        AND p.hire_date IS NULL
        AND sk.strength > 50
ORDER BY p.salary , p.age;

-- 7.	Detail info for all teams
select t.`name` as 'team_name', t.established, t.fan_base, count(p.id) as players_count from players as p
right join teams as t
on p.team_id = t.id
group by t.id
order by players_count desc, t.fan_base desc;

-- 8.	The fastest player by towns

select MAX(sd.speed) as 'max_speed', tw.name as 'town_name' from skills_data as sd
join players as p
on p.skills_data_id=sd.id
right join teams as t
on p.team_id = t.id
right join stadiums as s
on s.id = t.stadium_id
right join towns as tw
on tw.id = s.town_id
where t.name != 'Devify'
group by tw.id
order by max_speed desc, tw.name;

-- 9.	Total salaries and players by country
select c.name, count(p.id) as 'total_count_of_players', sum(p.salary) as 'total_sum_of_salaries' from players as p
left join teams as t
on p.team_id = t.id
join stadiums as s
on s.id = t.stadium_id
join towns as tw
on tw.id = s.town_id
right join countries as c
on tw.country_id = c.id
group by c.id
order by total_count_of_players desc, c.name;

-- 10.	Find all players that play on stadium
CREATE FUNCTION `udf_stadium_players_count` (stadium_name VARCHAR(30))
RETURNS INTEGER
BEGIN

RETURN (select count(p.id) from players as p
join teams as t
on p.team_id = t.id
right join stadiums as s
on s.id = t.stadium_id
where s.name = stadium_name
group by s.name);
END


-- 11. Find good playmaker by teams
CREATE PROCEDURE `udp_find_playmaker` (min_dribble_points int, team_name varchar(45))
BEGIN
	select concat(p.first_name,' ', p.last_name) as 'full_name', p.age, p.salary, sd.dribbling, sd.speed, t.name as 'team_name' from players as p
	join skills_data as sd
	on sd.id = p.skills_data_id
	join teams as t
	on t.id = p.team_id
	where sd.dribbling > min_dribble_points and t.name = team_name
	and sd.speed > (select avg(speed) from skills_data)
	order by sd.speed desc
	limit 1;

END



