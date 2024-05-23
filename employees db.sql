-- SELECT * FROM employees.departments;

-- SELECT dept_name FROM departments;

-- SELECT COUNT(emp_no) FROM employees;

-- SELECT dept_emp.*, departments.dept_name
-- FROM dept_emp
-- INNER JOIN departments
-- WHERE dept_emp.dept_no = departments.dept_no;

### 4/22

-- SELECT * FROM employees;

-- SELECT COUNT(*) FROM employees;

-- SELECT COUNT(emp_no) FROM employees;

-- SELECT 
--     COUNT(E.emp_no)
-- FROM
--     employees AS E
--         JOIN
--     salaries AS S ON E.emp_no = S.emp_no;

-- SELECT 
--     COUNT(E.emp_no)
-- FROM
--     employees AS E
--         JOIN
--     salaries AS S ON E.emp_no = S.emp_no
-- WHERE
--     S.to_date = '9999-01-01';

-- SELECT dept_emp.*, departments.dept_name
-- FROM dept_emp
-- INNER JOIN departments 
-- WHERE dept_emp.dept_no = departments.dept_no;

-- SELECT dept_emp.*, departments.dept_name, employees.first_name
-- FROM dept_emp
-- INNER JOIN
-- departments ON dept_emp.dept_no = departments.dept_no
-- INNER JOIN
-- employees ON dept_emp.emp_no = employees.emp_no;

-- SELECT E.emp_no, E.first_name, E.last_name, S.salary
-- FROM employees as E
-- INNER JOIN


### 4/24
#1
SELECT dept_name FROM departments;
SELECT DISTINCT(title) FROM titles;

#2
SELECT dept_no, COUNT(emp_no)
FROM
	employees.dept_emp
    GROUP BY dept_no;

#3
SELECT 
    DM.*, E.first_name, E.last_name
FROM
    dept_manager AS DM
	INNER JOIN 
    employees AS E ON DM.emp_no = E.emp_no
WHERE
    to_date = '9999-01-01';

#4
SELECT dept_name, COUNT(dept_emp.emp_no)
FROM departments
INNER JOIN
dept_emp
WHERE to_date = '9999-01-01'
GROUP BY departments.dept_name;

SELECT 
COUNT(dept_emp.emp_no), departments.dept_name
FROM
dept_emp
JOIN
departments ON dept_emp.dept_no = departments.dept_no
WHERE
dept_emp.to_date = '9999-01-01'
GROUP BY departments.dept_name;

#5
SELECT * FROM employees.salaries;

SELECT 
	*
FROM
    employees.salaries
WHERE
    to_date = '9999-01-01';

SELECT COUNT(*) FROM employees.salaries;

SELECT 
    COUNT(*)
FROM
    employees.salaries
WHERE
    to_date = '9999-01-01';
    
SELECT 
    D.dept_no, D.dept_name, E.emp_no, E.first_name, E.last_name, S.salary
FROM
    employees.salaries AS S
        JOIN
    employees AS E ON E.emp_no = S.emp_no
		JOIN
        dept_emp AS DE ON S.emp_no = DE.emp_no
        JOIN
        departments AS D ON DE.dept_no = D.dept_no
WHERE
    S.to_date = '9999-01-01'
		AND DE.to_date = '9999-01-01'
    ORDER BY D.dept_no;
    
#6

SELECT AVG(salary) FROM employees.salaries;

SELECT 
    D.dept_no, D.dept_name, AVG(salary)
FROM
    salaries AS S
        JOIN
    dept_emp AS DE ON S.emp_no = DE.emp_no
        JOIN
    departments AS D ON DE.dept_no = D.dept_no
WHERE
    S.to_date = '9999-01-01'
GROUP BY D.dept_no
ORDER BY D.dept_no;

SELECT 
    D.dept_no AS dep_no,
    D.dept_name AS dept_name,
    MAX(S.salary) AS max_salary,
    MIN(S.salary) AS min_salary,
    FORMAT(AVG(S.Salary), 2) AS avg_sal,
    FORMAT(SUM(S.salary), 2) AS sum_sal
FROM
    salaries AS S
        JOIN
    dept_emp AS DE ON S.emp_no = DE.emp_no
        JOIN
    departments AS D ON DE.dept_no = D.dept_no
WHERE
    S.to_date = '9999-01-01'
GROUP BY D.dept_no
ORDER BY D.dept_no;
