-- use world
-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. 
-- Your query should arrange the result by language percentage in descending order. (1)

-- SELECT * FROM countries
-- JOIN languages ON countries.id = languages.country_id
-- WHERE languages.language = "Slovene"
-- ORDER BY languages.percentage DESC;

-- "official answer for reference", my answer shows too much (though the question doesn't show ONLY return those). 
-- SELECT countries.name as name, languages.language as language, languages.percentage as percentage FROM countries
-- JOIN languages ON countries.id = languages.country_id
-- WHERE languages.language = "Slovene"
-- ORDER BY languages.percentage DESC;
-- 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. 
-- Your query should arrange the result by the number of cities in descending order. (3)
-- SELECT countries.name as name, count(cities.name) as cities
-- FROM COUNTRIES
-- join cities on countries.id = cities.country_id
-- group by countries.name
-- order by cities DESC;

-- does the material cover count?  

-- 
-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)

-- select * FROM cities 
-- WHERE country_code = "MEX" 
-- AND population >= 500000
-- order by cities.population DESC;


-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
-- i was close on this one, the issue I had was that I needed to pull from countries and join languages, becaue languages is linked to countries.  

-- SELECT countries.name as name, languages.language as language, languages.percentage as percentage from countries
-- join languages on countries.id = languages.country_id
-- where percentage > 89
-- ORDER BY languages.percentage DESC;

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT * FROM countries 
where population > 100000
and surface_area < 501;


-- 6. What query would you run to get countries with only Constitutional Monarchy governments, with a capital greater than 200 and a life expectancy greater than 75 years? (1)
-- select countries.name as country, countries.government_form as goverment_form, countries.capital as capital, countries.life_expectancy as life_expectancy
-- FROM countries
-- where countries.government_form = "Constitutional Monarchy"
-- and countries.capital > 200
-- and countries.life_expectancy > 75;
-- first try! whooooo

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? 
-- The query should return the Country Name, City Name, District and Population. (2)
-- select countries.name as name, cities.name as name, cities.district as district, cities.population as pop
-- from countries	
-- join cities ON countries.id = cities.country_id
-- where cities.district = "Buenos Aires"
-- and cities.population > 500000;
-- apparently i don't quite understand join, or what the ON operator does.   need to read more here

-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. 
-- Also, the query should arrange the result by the number of countries in descending order. (2)
SELECT countries.region as region, count(countries.name) as countries
from countries
group by countries.region;

-- this was a struggle, but I think I understand.  Count returns the number of rows selected, so by listing it AS countries that column becomes
-- the total number of countries.  without the groupby, which was something I just learned existed, it just puts the total number in the first result.
-- so it sets the names, pulls data from countries, and than groups by region and displays the result.  makes sense.  

-- Note: You may download this PDF file displaying the expected results from the queries