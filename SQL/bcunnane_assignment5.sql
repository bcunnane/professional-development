/* Assignment5.sql 
   BRANDON CUNNANE
   CS 31A, Summer 2022
*/

/* Set Database. */
USE bank;

/* Question 1: Write a query that uses a filter condition with a
noncorrelated subquery against the account type table to find all 
loan accounts (account_type.category_id= 'LOAN'). Display the 
account ID, type_id, client_id, and available balance.*/
SELECT account_id, type_id, client_id, avail_balance
FROM accounts
WHERE type_id IN (SELECT type_id FROM account_type WHERE category_id='LOAN');


/* Question 2: Rewrite the query from Question 1 using a correlated
subquery against the ACCOUNT_TYPE table to achieve the same results.*/
SELECT account_id, type_id, client_id, avail_balance
FROM accounts
WHERE EXISTS (SELECT type_id FROM account_type 
	WHERE accounts.type_id=type_id AND category_id='LOAN');


/* Question 3: Display the employee ID, first name, last name, and 
the department names and branch to which the employee is assigned.
Do not join any tables.*/
SELECT emp_id, first_name, last_name, 
(SELECT dept_name FROM department WHERE department.dept_id = employee.dept_id)
AS department_name, 
(SELECT branch_name FROM branch WHERE branch.branch_id = employee.branch_id)
AS branch_name
FROM employee;

/* Question 4: Display all teller employees at the San Francisco
branch. Display the employee ID and last name columns.*/
SELECT *
FROM employee
WHERE branch_id = (SELECT branch_id
				   FROM branch
				   WHERE branch_name = 'San Francisco Branch')
AND job_id = (SELECT job_id
			  FROM jobs
              WHERE job_title = 'Teller');


/* Question 5: Display employee IDs of all employees who supervise
other employees. Display employee ID, first name, last name, and 
job ID. Do not join any tables.*/
SELECT emp_id, first_name, last_name, job_id
FROM employee
WHERE emp_id IN (SELECT manager_id FROM employee);


/* Question 6: Display accounts with a total available balance
smaller than all of Richard Toby’s accounts. Display account ID, 
client ID, type ID, and available balance.*/
SELECT account_id, client_id, type_id, avail_balance
FROM accounts
WHERE avail_balance < (SELECT SUM(avail_balance)
					   FROM accounts a
					   JOIN individual_client ic 
                       ON (a.client_id = ic.client_id)
                       WHERE first_name = 'Richard' AND last_name = 'Toby');


/* Question 7: Display all saving accounts opened by a teller employee
at the San Francisco branch. Display account ID, type_id, and client ID.
Do not join any tables.*/
SELECT account_id, type_id, client_id
FROM accounts
WHERE type_id = 'SAV'
AND branch_id = (SELECT branch_id
				   FROM branch
				   WHERE branch_name = 'Headquarter');

/* Question 8: Display all the accounts for which a transaction was posted
on January 5, 2018. Display account ID, client ID, type ID, and available balance.*/
SELECT account_id, type_id, client_id, avail_balance
FROM accounts
WHERE account_id IN (SELECT account_id
					 FROM account_trans
                     WHERE trans_date = '2018-01-05');


/* Question 9: Display a list of department IDs along with the number of
employees assigned to each department. */
SELECT dept_id, dept_name, (SELECT COUNT(*)
						   FROM employee
                           WHERE department.dept_id = employee.dept_id)
                           AS num_employees
FROM department;


/* Question 10: Display data concerning all accounts that were NOT opened
by the head teller employee at the branch with the location ID 10001 */
SELECT account_id, type_id, client_id, avail_balance
FROM accounts
WHERE open_emp_id IN (SELECT emp_id
					  FROM employee e
                      JOIN branch b ON (e.branch_id = b.branch_id)
                      WHERE loc_id != 10001 AND job_id != 'HD_TEL');


/* Question 11: Use a subquery in the HAVING clause to find the employee
responsible for opening the most accounts.*/
SELECT open_emp_id, COUNT(*)
FROM accounts
GROUP BY open_emp_id
HAVING COUNT(*) = (SELECT MAX(c) 
				   FROM (SELECT open_emp_id, COUNT(*) AS c
						 FROM accounts
						 GROUP BY open_emp_id)
                         AS emp_open_counts);


/* Question 12: Find all accounts opened by experienced teller employees
who were hired before 2015 and are currently assigned to the Chicago branch.
Join the ACCOUNTS table to subqueries against the BRANCH and EMPLOYEE tables.*/
SELECT account_id, client_id, created, type_id
FROM accounts a
JOIN (SELECT * FROM branch WHERE branch_name='Chicago Branch') b
ON (a.branch_id = b.branch_id)
JOIN (SELECT * FROM employee WHERE start_date < '2015-01-01') e
ON (a.open_emp_id = e.emp_id);