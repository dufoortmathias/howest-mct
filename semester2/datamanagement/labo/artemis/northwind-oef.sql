use northwind;

#1
select o.id as OrderID, 
	concat(year(o.order_date), '-', month(o.order_date)) as DateOrdered, 
    customer_id as CustomerID, 
    concat(format(od.quantity * od.unit_price * (1-od.discount), '2C', 'be-be'), '€') as OrderPrice
from orders as o
join order_details as od on od.order_id = o.id
where o.id >= 70
order by od.quantity * od.unit_price * (1-od.discount) desc
;

#2
select o.id as OrderID, 
	concat(year(o.order_date), '-', month(o.order_date)) as DateOrdered, 
    customer_id as CustomerID, 
    concat(format(od.quantity * od.unit_price * (1-od.discount), '2C', 'be-be'), '€') as OrderPrice,
    p.product_name as ProductName,
    format(od.quantity, '0') as Quantity
from orders as o
join order_details as od on od.order_id = o.id
join products as p on od.product_id = p.id
where o.id >= 70
order by od.quantity * od.unit_price * (1-od.discount) desc
;

#3
select *
from orders as o
right join customers as c on o.customer_id = c.id
where o.customer_id is null
; 

#4
select *
from customers as c
where id in (
	select customer_id
    from orders
);

#6
(select concat(first_name, ' ', last_name) as ContactName,
	city as City,
    address as Address,
    'Customer' as TableName
from customers as c)
union
(select concat(first_name, ' ', last_name) as ContactName,
	city as City,
    address as Address,
    'Employee' as TableName
from employees as e)
order by city;






