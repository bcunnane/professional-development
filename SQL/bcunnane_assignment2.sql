/* Assignment2.sql 
   BRANDON CUNNANE
   CS 31A, Spring 2022
*/

/* put the database name into this command */
USE bank;

/* Query 1: accounts sorted by available balance */
SELECT account_id, type_id, created, avail_balance
FROM accounts
ORDER BY avail_balance DESC;

/* Query 2: account ID, type ID, and branch ID for all accounts */
SELECT account_id, type_id, branch_id
FROM accounts;

/* Query 3: all rows and columns for complete branch table */
SELECT *
FROM branch;

/* Query 4: display individual_client where id is 4345 */
SELECT *
FROM individual_client
WHERE client_id=4345;

/* Query 5: display dept ID and name */
SELECT dept_id AS "Department ID", dept_name AS "Department name"
FROM department;

/* Query 6: all employees without a manager */
SELECT emp_id, first_name, last_name, manager_id
FROM employee
WHERE manager_id IS NULL
LIMIT 5;

/* Query 7: Select all active accounts with balance > $5500 */
SELECT account_id, client_id, avail_balance
FROM accounts
WHERE a_status = "active" AND avail_balance > 5500;

/* Query 8: accounts with balance between $3000 & $5000 */
SELECT account_id, type_id, client_id, avail_balance
FROM accounts
WHERE avail_balance BETWEEN 3000 AND 5000;

/* Query 9: select accounts based on specific types */
SELECT account_id, type_id, client_id, avail_balance
FROM accounts
WHERE type_id = 'CHK' OR type_id = 'SAV' OR type_id = 'CD' OR type_id = 'MM';

/*  Query 10: select employees with last_name with F or G */
SELECT emp_id AS "Empl ID", first_name AS "First Name", last_name AS "Last Name"
FROM employee
WHERE last_name BETWEEN 'F' AND 'H';

/* Query 11: display all employees not managed by helen fleming */
SELECT emp_id, first_name, last_name, manager_id
FROM employee
WHERE manager_id != 184167702;

/* Query 12: Select clients whose address contains 'v' */
SELECT client_id, address
FROM clients
WHERE address LIKE '%v%';


