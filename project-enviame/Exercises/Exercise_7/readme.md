# Ejercisio 7

Enviame Backend  "Ejercicio 7"

## Query result

```
use example;

UPDATE employees
INNER JOIN countries ON employees.country_id = countries.id
INNER JOIN continents ON countries.continent_id = continents.id
SET 
    employees.salary = employees.salary + employees.salary * (continents.anual_adjustment/100)
WHERE
    employees.salary <= 5000

```
