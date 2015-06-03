-- SELECT FirstName, LastName, Title from employees;
-- SELECT * FROM employees WHERE City='Seattle';
-- SELECT * FROM employees WHERE City='London';
-- SELECT * FROM employees WHERE Title like '%Sales%';
-- SELECT * FROM employees WHERE Title like '%Sales%'  and TitleOfCourtesy='Ms.' or TitleOfCourtesy='Mrs.';
-- SELECT * FROM employees ORDER BY BirthDate ASC LIMIT 5;
-- SELECT * FROM employees ORDER BY HireDate ASC LIMIT 5;
-- SELECT * FROM employees WHERE ReportsTo is NULL;
-- SELECT rp.FirstName, rp.LastName, bss.FirstName, bss.LastName
-- FROM employees as rp
-- INNER JOIN employees as bss
-- ON rp.ReportsTo=bss.EmployeeID;

-- SELECT COUNT(FirstName) FROM employees WHERE  TitleOfCourtesy='Ms.' or TitleOfCourtesy='Mrs.';
-- SELECT COUNT(FirstName) FROM employees WHERE  TitleOfCourtesy!='Ms.' and TitleOfCourtesy!='Mrs.';
-- SELECT COUNT(EmployeeID), City FROM employees GROUP BY City;
-- SELECT OrderID, FirstName, LastName 
-- FROM orders
-- JOIN employees 
-- ON orders.EmployeeID=employees.EmployeeID;

-- SELECT OrderID, CompanyName
-- FROM orders JOIN shippers 
-- ON orders.ShipVia=shippers.ShipperID;

-- SELECT COUNT(OrderID), ShipCountry 
-- FROM orders GROUP BY ShipCountry;

-- SELECT FirstName,LastName,COUNT(orders.EmployeeID) as TotalServedOrders
-- FROM employees JOIN orders 
-- ON employees.EmployeeID==orders.EmployeeID 
-- GROUP BY orders.EmployeeID 
-- ORDER BY TotalServedOrders DESC LIMIT 1; 

-- SELECT CompanyName, COUNT(orders.CustomerID) as TotalOrders
-- FROM customers JOIN orders 
-- ON customers.CustomerID==orders.CustomerID 
-- GROUP BY customers.CustomerID 
-- ORDER BY TotalOrders DESC LIMIT 1; 

-- SELECT orders.OrderID, employees.Firstname, employees.LastName, customers.CompanyName as ForCompany
-- FROM orders 
-- JOIN employees ON employees.EmployeeID=orders.EmployeeID 
-- JOIN customers ON customers.CustomerID=orders.CustomerID; 

SELECT shippers.CompanyName as Shipper, customers.CompanyName as Customer
FROM orders 
JOIN shippers ON shippers.ShipperID=orders.ShipVia 
JOIN customers ON customers.CustomerID=orders.CustomerID;