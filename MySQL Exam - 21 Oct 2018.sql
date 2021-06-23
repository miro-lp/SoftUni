create schema colonial_journey_management_system_db;
use colonial_journey_management_system_db;

-- 2.	Section: Data 

create table `planets`
(`id` int primary key auto_increment,
`name` varchar(30) not null);

create table `spaceports`
(`id` int primary key auto_increment,
`name` varchar(50) not null,
`planet_id` int,
constraint fk_spacesports_planets
foreign key (`planet_id`) references `planets`(`id`));

create table `spaceships`
(`id` int primary key auto_increment,
`name` varchar(50) not null,
`manufacturer` varchar(30) not null,
`light_speed_rate` int default 0 );


create table `colonists`
(`id` int primary key auto_increment,
`first_name` varchar(20) not null,
`last_name` varchar(20) not null,
`ucn` char(10) not null unique,
`birth_date` date not null);

create table `journeys`
(`id` int primary key auto_increment,
`journey_start` datetime not null,
`journey_end` datetime not null,
`purpose` enum('Medical','Technical','Educational','Military'),
`destination_spaceport_id` int,
`spaceship_id` int,
constraint fk_journeys_spaceports
foreign key (`destination_spaceport_id`) references `spaceports`(`id`),
constraint fk_journeys_spaceships
foreign key (`spaceship_id`) references `spaceships`(`id`));

create table `travel_cards`
(`id` int primary key auto_increment,
`card_number` char(10) not null unique,
`job_during_journey` enum('Pilot','Engineer','Trooper','Cleaner','Cook'),
`colonist_id` int,
`journey_id` int,
constraint fk_travel_cards_colonists
foreign key (`colonist_id`) references `colonists`(`id`),
constraint fk_trvel_cards_journes
foreign key (`journey_id`) references `journeys`(`id`));

-- 01.	Data Insertion
insert into travel_cards (card_number, job_during_journey, colonist_id,  journey_id)
select (case 
when birth_date >'1980-01-01' then concat(date_format(birth_date,'%Y%d'),left(ucn,4))
else concat(date_format(birth_date,'%Y%c'),right(ucn,4))
end), (case
when id%2 = 0 then 'Pilot'
when id%3 = 0 then 'Cook'
else 'Engineer'
end) , id, left(ucn,1)  from colonists
where id between 96 and 100;

-- 02.	Data Update
update journeys
set purpose = (case
when id%2=0 then 'Medical'
when id%3=0 then 'Technical'
when id%5=0 then 'Educational'
when id%7=0 then 'Military'
else purpose
end);

-- 03.	Data Deletion

-- delete from colonists
-- where 

-- 04.Extract all travel cards

select card_number, job_during_journey from travel_cards
order by card_number;

-- 05. Extract all colonists

select id, concat(first_name,' ', last_name) as 'full_name', ucn from colonists
order by first_name, last_name, id;

-- 06.	Extract all military journeys

select id, journey_start,journey_end from journeys
where purpose = 'Military'
order by journey_start;

-- 07.	Extract all pilots
select c.id, concat(c.first_name,' ', c.last_name) as 'full_name'from colonists as c
join travel_cards as tc
on c.id = tc.colonist_id
where job_during_journey = 'Pilot'
order by c.id;

-- 08.	Count all colonists that are on technical journey

select count(c.id) from colonists as c
join travel_cards as tc
on c.id = tc.colonist_id
join journeys as j
on j.id = tc.journey_id
where j.purpose = 'Technical';

-- 09.Extract the fastest spaceship
select ss.name as 'spaceship_name', sp.name as 'spaceport_name' from spaceships as ss
join journeys as j
on j.spaceship_id = ss.id
join spaceports as sp
on j.destination_spaceport_id = sp.id
where ss.light_speed_rate = (select max(s.light_speed_rate) from spaceships as s);

--

-- 10.Extract spaceships with pilots younger than 30 years

select s.name, s.manufacturer from spaceships as s
join journeys as j
on j.spaceship_id = s.id
join travel_cards as tc
on j.id = tc.journey_id
join colonists as c
on tc.colonist_id = c.id
where (2019- year(c.birth_date)) < 30 and tc.job_during_journey = 'Pilot'
order by s.name;


-- 11. Extract all educational mission planets and spaceports
select p.name, sp.name from planets as p
join spaceports as sp
on p.id = sp.planet_id
join journeys as j
on sp.id = j. destination_spaceport_id
where j.purpose = 'Educational'
order by sp.name desc;

-- 12. Extract all planets and their journey count
select p.name, count(j.id) as 'journeys_count' from planets as p
join spaceports as sp
on p.id = sp.planet_id
join journeys as j
on sp.id = j. destination_spaceport_id
group by p.id
order by journeys_count desc, p.name;


-- 13.Extract the shortest journey
select j.id, p.name as 'planet_name', sp.name as 'spaceport_name', j.purpose as 'journey_purpose' from planets as p
join spaceports as sp
on p.id = sp.planet_id
join journeys as j
on sp.id = j. destination_spaceport_id
where  j.journey_end-j.journey_start = (select min( j1.journey_end-j1.journey_start) from journeys as j1);


-- 14.Extract the less popular job

select tc.job_during_journey as 'job_name' from travel_cards as tc
join journeys as j
on j.id = tc.journey_id
where j.journey_end-j.journey_start = (select max( j1.journey_end-j1.journey_start) from journeys as j1)
group by tc.job_during_journey
order by count(tc.job_during_journey)
limit 1;

-- 15. Get colonists count

CREATE FUNCTION `udf_count_colonists_by_destination_planet ` (planet_name VARCHAR (30))
RETURNS INTEGER
BEGIN

RETURN (select count(c.id) from planets as p
	join spaceports as sp
	on p.id = sp.planet_id
	join journeys as j
	on sp.id = j. destination_spaceport_id
	join travel_cards as tc
	on j.id = tc.journey_id
	join colonists as c
	on c.id = tc.colonist_id
	where p.name = planet_name);
END

-- 16. Modify spaceship


