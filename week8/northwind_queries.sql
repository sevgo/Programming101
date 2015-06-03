-- List all employees with their first name, last name and title.
SELECT FirstName, LastName, Title FROM employees;
-- List all employees from Seattle.
SELECT * FROM employees
WHERE City='Seattle';
-- List all employees from London.
SELECT * FROM employees
WHERE City='London';
-- List all employees that work in the Sales department.
SELECT * FROM employees
WHERE Title like '%Sales%';
-- List all females employees that work in the Sales department.
SELECT * FROM employees
WHERE Title like '%Sales%'  and TitleOfCourtesy='Ms.' or TitleOfCourtesy='Mrs.';
-- List the 5 oldest employees.
SELECT * FROM employees
ORDER BY BirthDate ASC LIMIT 5;
-- List the first 5 hires of the company.
SELECT * FROM employees
ORDER BY HireDate ASC LIMIT 5;
-- List the employee who reports to no one (the boss)
SELECT * FROM employees
WHERE ReportsTo is NULL;
-- List all employes by their first and last name, and the first and last name
-- of the employees that they report to.
SELECT rp.FirstName, rp.LastName, bss.FirstName, bss.LastName
FROM employees as rp
JOIN employees as bss ON rp.ReportsTo=bss.EmployeeID;
-- Count all female employees.
SELECT COUNT(FirstName) FROM employees
WHERE  TitleOfCourtesy='Ms.' or TitleOfCourtesy='Mrs.';
-- Count all male employees.
SELECT COUNT(FirstName) FROM employees
WHERE TitleOfCourtesy!='Ms.' and TitleOfCourtesy!='Mrs.';
-- Count how many employees are there from the different cities. For example,
-- there are 4 employees from London.
SELECT COUNT(EmployeeID), City FROM employees GROUP BY City;
-- List all OrderIDs and the employees (by first and last name) that have
-- created them.
SELECT OrderID, FirstName, LastName 
FROM orders JOIN employees 
ON orders.EmployeeID=employees.EmployeeID;
-- List all OrderIDs and the shipper name that the order is going to be shipped via.
SELECT OrderID, CompanyName
FROM orders JOIN shippers 
ON orders.ShipVia=shippers.ShipperID;
-- List all contries and the total number of orders that are going to be
-- shipped there.
SELECT COUNT(OrderID), ShipCountry 
FROM orders GROUP BY ShipCountry;
-- Find the employee that has served the most orders.
SELECT FirstName,LastName,COUNT(orders.EmployeeID) as TotalServedOrders
FROM employees JOIN orders 
ON employees.EmployeeID==orders.EmployeeID 
GROUP BY orders.EmployeeID 
ORDER BY TotalServedOrders DESC LIMIT 1;
-- Find the customer that has placed the most orders.
SELECT CompanyName, COUNT(orders.CustomerID) as TotalOrders
FROM customers JOIN orders 
ON customers.CustomerID==orders.CustomerID 
GROUP BY customers.CustomerID 
ORDER BY TotalOrders DESC LIMIT 1; 
-- List all orders, with the employee serving them and the customer, that has
-- placed them.
SELECT orders.OrderID, employees.Firstname, employees.LastName, customers.CompanyName as ForCompany
FROM orders 
JOIN employees ON employees.EmployeeID=orders.EmployeeID 
JOIN customers ON customers.CustomerID=orders.CustomerID;
-- List for which customer, which shipper is going to deliver the order.
SELECT shippers.CompanyName as Shipper, customers.CompanyName as Customer
FROM orders 
JOIN shippers ON shippers.ShipperID=orders.ShipVia 
JOIN customers ON customers.CustomerID=orders.CustomerID;
