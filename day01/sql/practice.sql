Employee
--------------
id
name
salary
department

-- Find a Employee earning more than 50000
Select * from employee where salary > 50000;

-- Find Second highest salary
Select * from employe order by salary desc;

--Find Employee count department-wise.
Select count(*) from employee group by department;