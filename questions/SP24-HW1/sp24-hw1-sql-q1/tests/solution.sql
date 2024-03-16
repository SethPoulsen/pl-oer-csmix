SELECT ProductName, BrandName, YearReleased
FROM Products
WHERE YearReleased > 2015 AND ProductName LIKE "%x%"
ORDER BY YearReleased DESC, ProductName ASC;