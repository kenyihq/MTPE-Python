USE classicmodels;

-- Grupo 1
-- Listar los 7 proveedores de productos a partir del registro número 5.

SELECT *
FROM products
LIMIT 4, 7;

-- Listar los 5 primeros registros de proveedores únicos de productos.

SELECT DISTINCT productVendor
FROM products
LIMIT 5;

-- Listar los proveedores únicos de productos.

SELECT DISTINCT productVendor
FROM products;

-- Listar los proveedores de productos que contengan la palabra Classics.

SELECT *
FROM products
WHERE productVendor LIKE '%Classics%';

-- Grupo 2
-- Listar y ordenar alfabéticamente los proveedores de productos/vehículos.

SELECT *
FROM products
ORDER BY productVendor;

-- Listar (nombre y precio) los 10 vehículos más económicos.

SELECT productName, buyPrice
FROM products
ORDER BY buyPrice ASC
LIMIT 10;

-- Listar (nombre y precio) los 10 vehículos más caros.

SELECT productName, buyPrice
FROM products
ORDER BY buyPrice DESC
LIMIT 10;

-- Listar alfabéticamente a los proveedores, asimismo permitir ver la variación de precios de menor a mayor de los correspondientes modelos de vehículos.

SELECT productVendor, productLine, buyPrice
FROM products
ORDER BY productVendor, buyPrice;

-- Filtrar lo requerido anteriormente para vehículos con stock entre 500 y 2000.

SELECT productVendor, productLine, buyPrice, quantityInStock
FROM products
WHERE quantityInStock > 500 AND quantityInStock < 2000
ORDER BY productVendor, buyPrice;

-- Grupo 3
-- Listar los vehículos cuyo modelo de año sea de la década de los 60s. Ordenar los resultados del más caro al más económico.

SELECT *
FROM products
WHERE productName LIKE '__6_%'
ORDER BY buyPrice DESC;

-- Listar los vehículos PickUp y ordenarlos por precio desde el más económico al de mayor precio.

SELECT *
FROM products
WHERE productName LIKE '%PickUp%'
ORDER BY buyPrice;

-- Grupo 4
-- Listar aquello clientes que no tengan una segunda linea en su dirección

SELECT *
FROM customers
WHERE addressLine2 IS null;

-- Listar los vehiculos PickUp cuyo precio sea menor a 100

SELECT *
FROM products
WHERE productName LIKE '%PickUp%' AND buyPrice < 100;

-- Listar a los clientes ques sea de la ciudad de Las Vegas

SELECT *
FROM customers
WHERE city='Las Vegas';

-- Listar a clientes que pertenezcan a las ciudades como Boston, London y Philadelphia

SELECT *
FROM customers
WHERE city in ('Boston', 'London', 'Philadelphia');

-- Listar a clientes que no pertenezcan a ciudades como Saint Petersburg, Sevilla ni Auckland.

SELECT *
FROM customers
WHERE city NOT IN ('Saint Petersburg', 'Sevilla', 'Auckland');