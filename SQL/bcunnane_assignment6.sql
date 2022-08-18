/* Assignment6.sql 
   BRANDON CUNNANE
   CS 31A, Summer 2022
*/

/* Set Database. */
USE bank;

/*Question 1: Create a view named MAJOR_CLIENTS that consists of the client ID, first name,
last name for every individual client. Write and execute the command to retrieve all the 
information from the MAJOR_CLIENTS view. */
CREATE OR REPLACE VIEW major_clients AS
SELECT client_id, first_name, last_name
FROM individual_client;

SELECT * FROM major_clients;


/*Question 2: Create a view named SUPERVISOR_VW that generates the supervisor’s name and employee
name. Write and execute the command to retrieve all the information from the SUPERVISOR_VW view*/
CREATE OR REPLACE VIEW supervisor_vw AS
SELECT CONCAT(m.first_name, ' ', m.last_name) AS superviser_name, 
	   CONCAT(e.first_name, ' ', e.last_name) AS employee_name
FROM employee e
JOIN employee m ON (e.manager_id = m.emp_id);

SELECT * FROM supervisor_vw;


/*Question 3: The bank president would like to have a report showing the branch name, location ID,
city of each branch, and the total balance of all accounts opened at the branch. Create a view named
BRANCH_SUMMARY_VW to generate the data. Write and execute the command to retrieve all the information
from the BRANCH_SUMMARY_VW view.*/
CREATE or REPLACE VIEW branch_summary_vw AS 
SELECT branch_name, loc_id, city AS branch_city, SUM(avail_balance) AS total_balance
FROM accounts a
JOIN branch b ON (a.branch_id = b.branch_id)
JOIN location l ON (b.loc_id = l.location_id)
GROUP BY branch_name;

SELECT * FROM branch_summary_vw;


/*Question 4: Define a view named CLIENT_VW and mandate that all bank clients may use it to access
clients data. Write and execute the command to retrieve all the information from the CLIENT_VW view.*/
CREATE OR REPLACE VIEW client_vw AS
SELECT client_id, CONCAT('ends in ', SUBSTRING(fed_id,-4,4)) AS fed_id, client_type_id, address, loc_id
FROM clients;

SELECT * FROM client_vw;


/*Question 5: Define a view named BUSINESS_CLIENT_VW that allows only business clients to be queried.
Write and execute the command to retrieve all the information from the BUSINESS_CLIENT_VW view.*/
CREATE OR REPLACE VIEW business_client_vw AS
SELECT *
FROM client_vw
WHERE client_type_id = 'B';

SELECT * FROM business_client_vw;


/*Question 6: Create a monthly report to show the number of employees, the total number of active accounts,
and the total number of transactions for each branch. Define a view named BRANCH_ACTIVITY_VW that creates
the report. Write and execute the command to retrieve all the information from the BRANCH_ACTIVITY_VW view.*/
CREATE OR REPLACE VIEW branch_activity_vw AS
SELECT branch_name, loc_id,
COUNT(DISTINCT emp_id) AS num_employees,
COUNT(DISTINCT account_id) AS num_active_accounts,
COUNT(DISTINCT trans_id) AS tot_transactions
FROM branch b
LEFT JOIN employee e ON (b.branch_id = e.branch_id)
LEFT JOIN account_trans t ON (b.branch_id = t.branch_id)
GROUP BY branch_name;

SELECT * FROM branch_activity_vw;


/*Question 7: If the ACCOUNT_TRANS table became large, the designers may decide to break it into two tables:
(1) a TRANSACTION_CURRENT table which holds data up to six months ago, and (2) a TRANSACTION_HISTORY table
which holds all data since the account was opened. If a client wants to see all transactions for a particular
account, you need to query both tables. Create a view named TRANSACTION_VW that queries both tables and combines
the results together. Write and execute the command to retrieve all the information from the ACCOUNT_TRANS view.*/
CREATE OR REPLACE VIEW transaction_current AS
SELECT *
FROM account_trans
WHERE trans_date > (SELECT DATE_SUB(MAX(trans_date), INTERVAL 6 MONTH) FROM account_trans);

CREATE OR REPLACE VIEW transaction_history AS
SELECT *
FROM account_trans
WHERE trans_date < (SELECT DATE_SUB(MAX(trans_date), INTERVAL 6 MONTH) FROM account_trans);

CREATE OR REPLACE VIEW transaction_vw AS
SELECT *
FROM transaction_current

UNION

SELECT *
FROM transaction_history;

SELECT * FROM transaction_vw;


/*Question 8: Create a view named BUSINESS_CLIENT_VW that joins the CLIENTS and BUSINESS_CLIENT tables so that
all the data for business clients can be easily queried. Write and execute the command to retrieve all the
information from the BUSINESS_CLIENT_VW view.*/
CREATE OR REPLACE VIEW business_client_vw AS
SELECT bc.client_id, bus_name, start_date, state_id, fed_id, address, loc_id, phone_number
FROM business_client bc
JOIN clients c ON (bc.client_id = c.client_id);

SELECT * FROM business_client_vw;