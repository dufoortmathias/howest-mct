use artemis;

-- 4.3: inleidingsoefeningen

select Productnummer, Productnaam, concat (prijspereenheid,' €') as 'VerkoopPrijs',
	concat(PrijsPerEenheid*Voorraad, ' stuks') as 'VoorraadWaarde', voorraad
    FROM tblproducten
    ORDER BY voorraadwaarde DESC;


SELECT naam, straat, postnr, saldo
from tblklanten
where saldo > 100;

-- dit is een comment

-- 4.4.2 Oefeningen op where:

#1

select klantnummer, naam, type, gemeente
from tblKlanten
where gemeente = "Tienen";

#2
select productnaam 
from tblproducten
where categorienummer = '1'; -- where categorienummerm = 1; lukt ook

#3
select naam
from tblKlanten
where postnr = 3600;
-- of
select naam
from tblKlanten
where postnr = 9000;

#4
select naam, saldo, type
from tblklanten
where type = 'p' and postnr = 3300 and saldo != 0;

#5
select naam, gemeente
from tblklanten
where gemeente = 'Leuven' or gemeente = 'Herent';

#6
select naam, straat, concat(gemeente, postnr) as 'Gemeente'
from tblklanten
where type = 'T' or type = 'W';

#7
select werknemerid, concat(familienaam, voornaam) as 'Volledige Naam', geboortedatum
from tblwerknemers
where geboortedatum < '1950-01-01';


-- 4.4.4: Oefeningen op operatoren
#1
select klantnummer, naam, straat, concat(postnr, gemeente) as 'Postnr & Gemeente'
from tblklanten;

#2 
select klantnummer, naam, straat, concat(postnr, gemeente) as 'Postnr & Gemeente', saldo
from tblklanten
where saldo between 150 and 300
order by saldo desc;
-- of:
select klantnummer, naam, straat, concat(postnr, gemeente) as 'Postnr & Gemeente', saldo
from tblklanten
where saldo >= 150 and saldo <= 300
order by saldo desc;

#3
select *
from tblwerknemers
where month(geboortedatum) between 6 and 7;
-- of:
select *
from tblwerknemers
where month(geboortedatum) >= 6 and month(geboortedatum) <= 7;

select *
from tblwerknemers
where month(geboortedatum) not between 6 and 7;

#5
select *
from tblwerknemers
where geboortedatum between '1960-01-01' and '1966-01-27';

#6
select *
from tblklanten
where gemeente in ('Leuven', 'Herent',  'Kessel-Lo', 'Heverlee');

#7
select *
from tblklanten
where gemeente not in ('Leuven', 'Herent',  'Kessel-Lo', 'Heverlee');


#8
select *
from tblproducten
where categorienummer in (1, 2, 3, 4, 8)
order by categorienummer, nederlandsenaam;


-- 4.4.6: Oefeningen op like
#1
select *
from tblproducten
where nederlandsenaam like '%thee%';

#2
select *
from tblproducten
where nederlandsenaam like '%vlees%' or nederlandsenaam like '%kaas%';

#3
select *
from tblproducten
where (nederlandsenaam like '%vlees%' or nederlandsenaam like '%kaas%')
and prijsPerEenheid < 32;

#4
select concat(naam, ' uit ', gemeente) as "Klantnaam", gemeente
from tblklanten
where naam like 'Vander%';

#5
select concat(naam, ' uit ', gemeente) as "Klantnaam", gemeente
from tblklanten
where naam like 'Vander%t';

#6
select *
from tblklanten
where straat like '%dorp%';

#7
select *
from tblleveranciers
where bedrijf like '%an%' or bedrijf like '%foot%';

-- 4.4.9: Oefeningen op regexp
#1
select productnummer, productnaam
from tblproducten
where productnaam regexp '^chef.*mix$';

#2
select productnaam
from tblproducten
where productnaam regexp binary 'c'
order by productnaam;

#3
select productnaam
from tblproducten
where productnaam regexp binary '[cyB]'
order by productnaam;

#4
select *
from tblklanten
where saldo regexp '^.{4}$';

#5
select *
from tblbtwtarief
where btwpercentage regexp '[0-9]\.[0-9]{2}';

-- 4.5.2: Oefeningen op sorteren
#1
select *
from tblklanten
where type regexp '[wt]'
order by naam;

#2
select *
from tblklanten
where type regexp '[wt]'
order by type desc;

#3
select saldo, klantnummer, gemeente
from tblklanten
where saldo != 0
order by saldo desc;

#4
select concat(familienaam, voornaam) as 'Naam', geboortedatum
from tblwerknemers
order by geboortedatum;


-- 4.8: Oefeningen op select queries

#1
SELECT DISTINCT Familienaam, Voornaam, Gemeente, InDienst
FROM tblwerknemers
WHERE year(InDienst) = 1993
ORDER BY Indienst ASC;

#2
SELECT Naam, Gemeente
FROM tblklanten
Where Gemeente = "Leuven"
ORDER BY Naam ASC;

#3
SELECT Familienaam, Voornaam, Geslacht
FROM tblwerknemers
WHERE Geslacht = 2 AND Gemeente = "Leuven";

#4
SELECT Familienaam, Voornaam, Geslacht
FROM tblwerknemers
WHERE Geslacht = 1 AND Gemeente NOT IN ("Kessel-lo, Herent, Leuven");

#5
SELECT Klantnummer, Naam
FROM tblklanten
WHERE saldo > 175
ORDER BY Naam ASC;

#6
SELECT Klantnummer, Naam
FROM tblklanten
WHERE Naam REGEXP "^Van"
ORDER BY Naam ASC;

#7
SELECT upper(Gemeente) as "GEMEENTE", upper(Familienaam) as "FAMILIENAAM"
FROM tblwerknemers
WHERE Gemeente NOT IN ("Leuven", "Herent", "Peer", "Genk") AND Functie = "Vertegenwoordiger"
ORDER BY Gemeente;

#8
SELECT Productnaam, Voorraad, InBestelling, Bestelpunt,
Voorraad-InBestelling AS "Dringende-Tekorten"
FROM tblproducten
WHERE Voorraad-InBestelling < 0 OR Voorraad - InBestelling < Bestelpunt
ORDER BY Voorraad-InBestelling ASC;

#9
SELECT DISTINCT concat(upper(Bedrijf), " uit ", upper(Land)) AS "BEDRIJF en LAND"
FROM tblleveranciers
WHERE Land NOT IN ("Spanje", "Verenigd Koninkrijk")
ORDER BY bedrijf
LIMIT 5;

#10
SELECT DISTINCT Land
FROM tblleveranciers
ORDER BY Land;


-- 4.9.2: Oefeningen op aggregatiefuncties
#1
SELECT count(klantnummer) AS "Aantal klanten",
sum(Saldo) AS "Saldo"
FROM tblklanten
WHERE ondernemingsnr IS NOT NULL;

#2
SELECT count(OrderID) AS "Aantal orders"
FROM tblorders
WHERE date(Orderdatum) = "2006-08-06";

#3
SELECT avg(prijspereenheid * 1.1) AS "Gemiddelde prijs per eenheid"
FROM tblProducten;

#4
SELECT count(werknemerID) AS "Aantal vertegenwoordigers"
FROM tblwerknemers
WHERE Functie = "Vertegenwoordiger" AND InDienst < "1993-01-01";

#5
SELECT timestampdiff(year, min(geboortedatum), max(geboortedatum)) AS "Verschil in jaren"
FROM tblwerknemers
WHERE gemeente = "Leuven";

#6
SELECT count(OrderID) AS "Aantal orders"
FROM tblorders
WHERE Orderdatum BETWEEN "2005-01-01" AND "2006-01-01";

#7
SELECT avg(Brutowedde) AS "Gemiddelde brutowedde"
FROM tblwerknemers;

#8
SELECT count(WerknemerID) AS "Aantal mannen"
FROM tblwerknemers
WHERE geslacht = 1;
I will keep this updated. Thank you all a lot and don't worry, we aren't done in here just yet.
#9
SELECT max(prijspereenheid) - min(prijspereenheid) AS "Verschil"
FROM tblproducten;

#10
SELECT count(klantnummer) AS "Aantal klanten"
FROM tblklanten
WHERE Gemeente = "Brussel";

-- 4.12: Oefeningen op datums en NULL
#1
SELECT OrderID,Leverdatum
FROM tblorders
WHERE Leverdatum IS NULL;

#2
SELECT avg(timestampdiff(day,Orderdatum, Leverdatum)) as "Gemiddelde leverduur"
FROM tblorders;

#3
SELECT OrderID, Klantnummer, dayname(Leverdatum) AS "Day of the week"
FROM tblorders
WHERE dayname(Leverdatum) NOT IN ("Monday", "Friday");

#4
SELECT OrderID, Klantnummer,
dayname(Leverdatum) AS "Day of the week",
dayofweek(Leverdatum) AS "day Index"
FROM tblorders
WHERE Leverdatum IS NOT NULL
ORDER BY dayofweek(Leverdatum), OrderID;

#5
SELECT count(WerknemerID) AS "Aantal vrouwelijke werknemers",
avg(timestampdiff(YEAR, Geboortedatum, NOW())) AS "Gemiddelde leeftijd"
FROM tblwerknemers
WHERE Geslacht = 2;

#6
SELECT count(WerknemerID) AS "Aantal vrouwelijke werknemers",
round(avg(timestampdiff(YEAR, Geboortedatum, NOW())), 1) AS "Gemiddelde leeftijd"
FROM tblwerknemers
WHERE Geslacht = 2;

-- 4.14.1: Oefeningen op GROUP BY en HAVING
#1
select categorienummer, concat(count(*), ' stuks') as 'Aantal Producten'
from tblproducten
where prijspereenheid > 50
group by categorienummer
order by 'Aantal Producten';

#2
select Gemeente, concat(count(*), ' klanten') as 'Aantal Klanten'
from tblklanten
group by Gemeente
order by count(*) desc;

#3
select Gemeente, concat(count(*), ' klanten') as 'Aantal Klanten'
from tblklanten
group by Gemeente
having count(*) > 3
order by count(*) desc;

#4
select count(*), functie
from tblwerknemers
group by functie
order by count(*) desc;

#5
select count(*), geslacht, functie
from tblwerknemers
group by functie, geslacht
order by count(*) desc;
-- betere formatting met case-statement:
-- select count(*), case geslacht when geslacht = 1 then 'Man' else 'Vrouw' end, functie
-- from tblwerknemers
-- group by functie, geslacht
-- order by count(*) desc;

#6
select count(*) as 'Klanten zonder ondernemingsnr'
from tblklanten
where ondernemingsnr is null;

#7
select categorienummer, concat(count(*), ' stuks') as 'Aantal Producten', concat(format(sum(voorraad * prijspereenheid), '2'),' €') as 'Voorraadwaarde'
from tblproducten
group by categorienummer
order by categorienummer;


#8
select categorienummer, leveranciersnummer, concat(count(*), ' stuks') as 'Aantal Producten', concat(format(sum(voorraad * prijspereenheid), '2'),' €') as 'Voorraadwaarde'
from tblproducten
where leveranciersnummer = 4
group by categorienummer
order by categorienummer;

#9
select categorienummer, leveranciersnummer, concat(count(*), ' stuks') as 'Aantal Producten', concat(format(sum(voorraad * prijspereenheid), '2'),' €') as 'Voorraadwaarde'
from tblproducten
where leveranciersnummer = 6
group by categorienummer
having sum(voorraad * prijspereenheid) > 1000;

#10
select year(orderdatum) as 'Jaartal', concat(format(avg(datediff(leverdatum, orderdatum)), 0), ' dagen') as 'Levertermijn'
from tblorders
group by year(orderdatum)
order by datediff(leverdatum, orderdatum) desc;

-- 4.15: Oefeningen op controlestructuren
#1
select familienaam, voornaam, concat('beschikt ', if(auto=1, '', 'NIET '), 'over een firmawagen') as 'Firmawagen?'
from tblwerknemers;

#2
select *, if(leverdatum is null and vrachtkosten is null, 'Nog niet geleverd', 'Geleverd') as 'Geleverd?'
from tblorders
where leverdatum is null and vrachtkosten is null;



-- 5.2.2: Oefeningen op subqueries
#1
select nederlandsenaam, prijspereenheid,  voorraad, (prijspereenheid * voorraad) as 'voorraadwaarde'
from tblproducten
where (prijspereenheid * voorraad) > (select
	min(brutowedde)
    from tblwerknemers
)
group by nederlandsenaam;

#2
select naam, gemeente, postnr, straat
from tblklanten
where naam in (
	select familienaam
    from tblwerknemers
);

#3
select naam, gemeente, postnr, straat
from tblklanten
where klantnummer in (
	select klantnummer
    from tblorders
    where datediff(orderdatum, leverdatum) <= 31
    and year(leverdatum) = 2006
);


#4
select *
from tblproducten
where productnummer in (
	select productnummer
    from tblorderinformatie
    where korting >= 0.25
);

#5
select concat(voornaam, ' ', familienaam) as 'Volledige naam'
from tblwerknemers
where werknemerid not in (
	select werknemerid
    from tblorders
)
order by 'Volledige naam';

#6
select familienaam, indienst
from tblwerknemers
where indienst between (
	select indienst
    from tblwerknemers
    where familienaam like 'Smets'
    limit 1
) and (
	select indienst
    from tblwerknemers
    where familienaam like 'Daponte'
    limit 1
);


-- 5.3.5.1: Oefeningen op JOINS, SUBQUERIES en AGGREGATIES
-- oefeningen op artemis
#1
select c.Categorienaam, c.Categorienummer, (p.Voorraad - p.inbestelling) as 'Tekort'
from tblproducten p
join tblcategorieen c using(categorienummer)
where InBestelling > voorraad
order by Categorienaam;


#2
select land, bedrijf, concat(count(productnummer), ' producten') as 'Aantal producten'
from tblleveranciers
join tblproducten using(leveranciersnummer)
group by bedrijf
order by land, bedrijf;

#3
select p.categorienummer, count(l.Leveranciersnummer) as 'Aantal leveranciers'
from tblproducten p
join tblleveranciers l using(Leveranciersnummer)
group by categorienummer;


#4
select btwcode, BTWPercentage
from tblproducten p
right join tblbtwtarief b using(btwcode)
where p.Productnummer is null;

#5
select *
from tblproducten
left join tblorderinformatie using(productnummer)
where tblorderinformatie.orderid is null;

#6
select familienaam, format(sum(prijspereenheid * Hoeveelheid * (1-korting)), '2')
from tblwerknemers
left join tblorders using(werknemerid) 
left join tblorderinformatie using(orderid)
left join tblproducten using(productnummer)
group by familienaam
order by sum(prijspereenheid*tblorderinformatie.hoeveelheid) desc;


#7a
select *
from tblleveranciers as l
left join tblproducten as p using(leveranciersnummer)
where p.leveranciersnummer is null;

#7b
select *
from tblproducten
left join tblcategorieen using(categorienummer)
where tblcategorieen.categorienummer is null;

#7c
select * 
from tblklanten
left join tblorders using(klantnummer)
where tblorders.klantnummer is null;

#7d
select count(*)
from tblorders
left join tblwerknemers using(werknemerid)
where tblorders.werknemerid is null;

#7e
select *
from tblverzenders
left join tblorders using(verzendid)
where tblorders.verzendid is null;


-- 6.1.3: Oefeningen op UPDATE volgens een filter in dezelfde tabel
#1
-- query om de wijzigingen te controleren:
select *
from tblorderinformatie
where orderid = 11078;

-- update query
update tblorderinformatie
set hoeveelheid = hoeveelheid + 5
where orderid = 11078;

#2
select *
from tblklanten
where saldo > 1000;

update tblklanten
set saldo = saldo * 1.10
where saldo > 1000;

#3
select *
from tblklanten
where naam regexp 'Vandeput$';

update tblklanten
set straat = 'Zandloperstraat 9',
	postnr = 9030,
	gemeente = 'Mariakerke'
where naam regexp '^Vandeput$';

#4
update tblorders
set vervaldatum = date_add(leverdatum, INTERVAL 5*rand() DAY)
where datediff(leverdatum, vervaldatum) > 10 and vervaldatum < leverdatum;

#5
update tblWerknemers
set geslacht = case
	when geslacht = 1 then 'M'
    else 'V'
end;

-- 6.2: Oefeningen op UPDATE volgens een filter in een gerelateerde tabel
#1
select count(*)
from tblproducten
join tblorderinformatie using(productnummer)
where voorraad >= 123;

update tblorderinformatie
right join tblproducten using(productnummer)
set korting = 0.25
where voorraad >= 123;

-- 7.5: Oefeningen op DELETE
#1: klanten die geen orders hebben
#1.1
select *
from tblklanten
left join tblorders using(klantnummer)
where tblorders.klantnummer is null;

#1.2
delete from tblklanten
where klantnummer = 1;


#1.3
delete from tblklanten
where klantnummer in (
	select klantnummer
	from tblklanten
	left join tblorders using(klantnummer)
	where tblorders.klantnummer is null
)
limit 3;

#1.4
select count(*)
from tblklanten
left join tblorders using(klantnummer)
where tblorders.klantnummer is null;

#2 klanten die wel orders geplaatst hebben
#2.1
select klantnummer, count(orderid)
from tblklanten
join tblorders using(klantnummer)
group by klantnummer
order by count(orderid)
limit 1;

#2.2
delete from tblklanten
where klantnummer = (
	select klantnummer
    from tblklanten
    join tblorders using(klantnummer)
	group by klantnummer
	order by count(orderid)
	limit 1
);

#Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`artemis`.`tblorders`, CONSTRAINT `FK_tblOrders_tblKlanten` FOREIGN KEY (`Klantnummer`) REFERENCES `tblklanten` (`Klantnummer`))
# Deze error ontstaat omdat er in de tabel tblOrders nog klantnummers bestaan.

#2.3
# Vorige oefening is op te lossen als je het delete type op bv 'Set NULL' zet.

#2.4
# volg de stappen op p84 in de cursus om het delete type van tblKlanten te veranderen.
delete from tblklanten
where klantnummer = (
	select klantnummer
    from tblklanten
    join tblorders using(klantnummer)
	group by klantnummer
	order by count(orderid)
	limit 1
);

#2.5a: 10 producten
select *
from tblproducten 
join tblcategorieen using(categorienummer)
where tblcategorieen.categorienaam like 'zuivel';

#2.5b
update tblproducten
join tblcategorieen using(categorienummer)
set uitassortiment = 1
where tblcategorieen.categorienaam like 'zuivel';

delete tblcategorieen
from tblproducten
join tblcategorieen using(categorienummer)
where categorienaam like 'zuivel';

#2.5c
# ?

#2.6
delete tblorderinformatie
from tblorderinformatie
join tblorders o using(orderid)
join tblwerknemers w using(werknemerid)
where w.familienaam = "Davidson" and o.leverdatum = '2006-05-22';


-- 9.1: Oefeningen op DELETE, INSERT, en UPDATE
#1
INSERT INTO tblklanten (Naam, Straat, Postnr, Gemeente, Ondernemingsnr)
VALUES ('Howest', 'Graaf Karel de Goedelaan 5', '8500', 'Kortrijk', '102-213-123');

#2
create table tblVlees
	select *
    from tblproducten
    where categorienummer = 6;

#3
delete tblVlees
from tblVlees
where voorraad = 0;

select *
from tblVlees;

#4
insert into tblwerknemers (familienaam, voornaam, auto)
values ('Vanhoutte', 'Tuur', 1);

#5
insert into tblorders (klantnummer, werknemerid, orderdatum)
values (
	(select klantnummer from tblklanten where naam = 'Howest'),
    (select werknemerid from tblwerknemers where familienaam = 'Vanhoutte' and voornaam = 'Tuur'),
    now()
);

#6
DELETE tblorders FROM tblorders
        JOIN
    tblklanten USING (klantnummer) 
WHERE
    tblklanten.naam = 'Howest'
    AND DATE(NOW()) = DATE(tblorders.orderdatum);

#7
create table tblproducten_backup
	select *
    from tblproducten;

UPDATE tblproducten_backup 
SET 
    prijspereenheid = prijspereenheid * 1.10
WHERE
    productnaam = 'Tofu';

UPDATE tblproducten_backup 
SET 
    prijspereenheid = CASE
        WHEN categorienummer = 6 THEN prijspereenheid * 0.95
        WHEN categorienummer = 5 THEN prijspereenheid * 1.06
    END;

UPDATE tblproducten 
SET 
    prijspereenheid = CASE
        WHEN categorienummer = 6 THEN prijspereenheid * 0.95
        WHEN categorienummer = 5 THEN prijspereenheid * 1.06
    END;

-- 10.2: Oefeningen op views

-- Plak deze sql statements in de create view wizard (rechtermuisknop op 'Views' in het linkerscherm -> create view...)

#1
SELECT 
    c.Categorienaam AS 'Category Name',
    c.Categorienummer AS 'Category Number',
    p.Productnummer AS 'Product Number',
    p.Productnaam AS 'Product Name',
    p.NederlandseNaam AS 'Dutch Name',
    p.Leveranciersnummer AS 'Supplier Number',
    p.HoeveelheidPerEenheid AS 'Unit Quantity',
    p.PrijsPerEenheid AS 'Unit Price',
    p.Voorraad AS 'Stock Quantity',
    p.BTWCode AS 'BTWCode',
    p.InBestelling AS 'On Order',
    p.Bestelpunt AS 'Orderpoint',
    p.UitAssortiment AS 'No longer available'
FROM
    tblproducten p
        JOIN
    tblcategorieen c USING (categorienummer)
WHERE
    c.Categorienaam LIKE 'fruit%';

#2
    SELECT 
    categorienaam AS 'Categorienaam',
    productnaam AS 'Productnaam',
    CONCAT('€', FORMAT(prijspereenheid, '2')) AS 'Prijs'
FROM
    tblproducten
        JOIN
    tblcategorieen USING (categorienummer)
GROUP BY productnaam
ORDER BY categorienaam , prijspereenheid DESC;


#3
insert into tblproducten (productnaam, uitassortiment, prijspereenheid)
values ('testProduct', 0, 20.00);

SELECT 
    categorienaam AS 'Categorienaam',
    productnaam AS 'Productnaam',
    CONCAT('€', FORMAT(prijspereenheid, '2')) AS 'Prijs'
FROM
    tblproducten
        LEFT JOIN
    tblcategorieen USING (categorienummer)
ORDER BY categorienaam , prijspereenheid DESC;

