-- Soal #1.1
select * from city;
SELECT ID, Name, CountryCode, District, Population from city
where CountryCode = 'IDN'
ORDER BY Population desc
limit 10;

-- Soal #1.2
select  city.id, city.Name as nama_kota,  city.District as district, country.name as negara, country.Population
from city inner join country
on city.CountryCode = country.Code
ORDER BY city.population desc
limit 10; 

-- Soal #1.3
select distinct country.Code, country.Name, country.Continent, country.region, country.IndepYear as tahun_merdeka
from country inner join city
on city.CountryCode = country.Code
where country.IndepYear is not null
ORDER BY country.Indepyear ASC
limit 10; 

-- Soal #1.4
select country.Continent, count(country.Continent) as Jumlah_Negara,  country.Population as Populasi, AVG(LifeExpectancy) as Rata_AngkaHrpnHdp
from country
GROUP BY Continent
HAVING COUNT(Continent) > 10
ORDER BY country.Continent ASC;

-- Soal #5 
select country.name as Nama, country.Continent as Benua, country.LifeExpectancy as AngkaHarapanHidup, country.GNP
from country
where country.Continent = 'Asia'
ORDER BY country.LifeExpectancy desc;

-- Soal #1.6
 select * from countrylanguage;
select countrylanguage.CountryCode, country.name, countrylanguage.Language, countrylanguage.IsOfficial, countrylanguage.Percentage
from countrylanguage inner join country
on countrylanguage.CountryCode = country.Code
where countrylanguage.Language = 'English' and countrylanguage.IsOfficial = 'T'
order by countrylanguage.Percentage desc
limit 10;

-- Soal #1.7
CREATE TABLE CapitalCity
  SELECT country.Capital as Capital_ID, city.Name as Capital_Name, city.Population, city.CountryCode
  from country join city 
  on country.Capital = city.ID;

select * from capitalcity;

select country.name as Negara_ASEAN, country.Population as Populasi_Negara, 
country.GNP, capitalcity.Capital_Name as Ibukota, capitalcity.Population as Populasi_Ibukota
from country join capitalcity
on country.Capital = capitalcity.Capital_ID 
where country.Region = 'Southeast Asia' 
group by country.name;

-- Soal #1.8

CREATE TABLE `world`.`g20_list` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
  ALTER TABLE `world`.`g20_list` 
CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT ;

INSERT INTO `world`.`g20_list` (`name`) VALUES ('Argentina');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Australia');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Brazil');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Canada');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('China');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('France');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Germany');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('India');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Indonesia');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Italia');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Japan');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Mexico');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Russian Federation');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Saudi Arabia');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('South Africa');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('South Korea');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('Turkey');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('United Kingdom');
INSERT INTO `world`.`g20_list` (`name`) VALUES ('United States');

select * from g20_list;
	
select g20_list.name as Negara_G20, country.Population as Populasi_Negara, country.GNP, capitalcity.Capital_Name as Ibukota, capitalcity.Population as Populasi_Ibukota
from g20_list join country
on g20_list.name = country.name
join capitalcity
on country.Capital = capitalcity.Capital_ID 
order by country.GNP desc 
limit 20;


-- buat database ASEAN untuk Soal #2 

create table ASEAN
select country.name as Negara_ASEAN, country.Population as Populasi_Negara, 
country.GNP, capitalcity.Capital_Name as Ibukota, capitalcity.Population as Populasi_Ibukota, country.SurfaceArea
from country join capitalcity
on country.Capital = capitalcity.Capital_ID 
where country.Region = 'Southeast Asia' 
group by country.name; 
select * from asean;