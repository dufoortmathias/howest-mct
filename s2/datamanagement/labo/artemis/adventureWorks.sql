##############################
########AdventureWorks########
##############################
use adventureworks2014;

-- 4.16.1: Oefeningen queries op adventureworks
#1
select firstname, middlename, lastname, BusinessEntityID
from person
where middlename regexp 'J' -- om zowel 'J' als 'J.' te matchen
and (lastname like 'alexander' or lastname like 'zhang');

#2
select productid, name, color, size
from product
where size is null or color is null;

#3
select count(*) as 'aantal', avg(size) as 'gemiddelde grootte'
from product
where size is not null and color is not null;

#4
select concat(firstname, case when middlename is null then ' ' else concat(' ', middlename, ' ') end, lastname) as 'Full name'
from person
where lastname regexp '^v|^w'
limit 1500; -- standaardlimiet is 1000, maar er zijn meer rijen

#5
select concat(businessentityid, ': ' ,firstname, case when middlename is null then ' ' else concat(' ', middlename, ' ') end, lastname) as 'Full name'
from person
where lastname regexp '^v|^w'
order by businessentityid
limit 1500; -- standaardlimiet is 1000, maar er zijn meer rijen

#6
select firstname
from person
where firstname = reverse(firstname);

#7
select substring(emailaddress, locate('@', EmailAddress) + 1)
from productreview;

#8
select distinct(jobtitle)
from employee
order by jobtitle;

#9
select distinct concat(firstname, ' ', lastname) as fullname
from person
where firstname regexp 'k';
