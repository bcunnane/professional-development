/* Assignment4.sql 
   BRANDON CUNNANE
   CS 31A, Summer 2022
*/

/* Set Database. */
USE bank;

/* Question 1: For all accounts opened on May 23, 2015, write a SQL 
statement that lists the account ID, created dat, and client ID. */
SELECT account_id, created, client_id
FROM accounts
WHERE created = '2015-05-23';

/* Question 2: For all accounts, write a SQL statement that lists 
the account ID, created date, type ID, account name, and category 
ID for each type that make up the account. Order the rows by
category ID and then by account ID. */
SELECT a.account_id, a.created, a.type_id, t.account_name, t.category_id
FROM accounts a, account_type t
WHERE a.type_id = t.type_id
ORDER BY t.category_id, a.account_id;

/* Question 3: Display the account ID, created date, type ID, account
name, and client ID for each account that is not a “checking account”.*/
SELECT A.account_id, A.created, a.type_id, t.account_name, a.client_id, t.account_name
FROM accounts a 
JOIN account_type t ON (a.type_id = t.type_id)
WHERE t.account_name != 'checking account';

/* Question 4: Display all accounts names along with account IDs. (Use the
type_id column in the accounts table to link to the ACCOUNT_TYPE table).
Include all accounts, even if no accounts have been opened for that type.*/
SELECT t.type_id, a.account_id, a.client_id, a.avail_balance, t.account_name
FROM account_type t
LEFT JOIN accounts a
ON (a.type_id = t.type_id); 

/*Question 5: Display all accounts opened by experienced tellers who were hired
prior to January 1, 2007 and currently assigned to the Chicago branch. Display
account ID, client ID, created date, and type ID.*/
SELECT a.account_id, a.client_id, a.created, a.type_id
FROM accounts a
JOIN employee e ON (a.open_emp_id = e.emp_id)
JOIN branch b ON (e.branch_id = b.branch_id)
WHERE start_date < '2007-01-01' AND branch_name = 'Chicago Branch';

/*Question 6: Display the account id and federal tax number for all 
non-business accounts.*/
SELECT a.account_id, c.fed_id, ic.first_name, ic.last_name
FROM accounts a
JOIN clients c ON (a.client_id = c.client_id)
JOIN individual_client ic ON (a.client_id = ic.client_id);

/*Question 7: Use the UNION ALL operator to generate a full set 
of client data from the INDIVIDUAL_CLIENT and BUSINESS_CLIENT tables*/
SELECT client_id, last_name AS 'name'
FROM individual_client
UNION ALL
SELECT client_id, bus_name
FROM business_client;

/*Question 8: Display all accounts along with either the first name and
last name of individual clients OR the business name of business clients.*/
SELECT a.account_id, a.type_id, 
concat(ic.first_name, ' ', ic.last_name) AS 'person_name', 
bc.bus_name AS 'business_name'
FROM accounts a
LEFT JOIN individual_client ic ON (a.client_id = ic.client_id)
LEFT JOIN business_client bc ON (a.client_id = bc.client_id);

/*Question 9: Display the account ID, client last name, federal ID,
and account names. Display the first 10 rows in the result set.*/
SELECT account_id, last_name, fed_id, account_name
FROM accounts a
JOIN individual_client ic ON (a.client_id = ic.client_id)
JOIN clients c ON (a.client_id = c.client_id)
JOIN account_type t ON (a.type_id = t.type_id)
LIMIT 10;

/*Question 10: Display the total available balance by account type
and branch where there is more than one account per type and branch. 
Order the results by total balance (highest to lowest).*/
SELECT type_id, branch_id, SUM(avail_balance) AS total
FROM accounts
GROUP BY type_id, branch_id
HAVING COUNT(*) > 1
ORDER BY total DESC;

/*Question 11: You are in charge of operations at the bank, and you 
would like to find out how many accounts are being opened by each 
bank teller employee. Display open employee ID and how many accounts 
each teller employee opened.*/
SELECT open_emp_id, COUNT(*)
FROM accounts
GROUP BY open_emp_id;

/*Question 12: Display any cases where an employee has opened fewer 
than five accounts.*/
SELECT open_emp_id, COUNT(*)
FROM accounts
GROUP BY open_emp_id
HAVING COUNT(*) < 5;

/*Question 13: Display the total balances not only for each account, 
but for both types and branches (e.g., What is the total balance for 
all checking accounts opened at the San Francisco branch?). Filter out 
any type with a total available balance less than $10,000.*/
SELECT type_id, branch_id, SUM(avail_balance)
FROM accounts
GROUP BY type_id, branch_id
HAVING SUM(avail_balance) >= 10000;

/*Question 14: Display any type with a total available balance 
greater than $10,000.*/
SELECT type_id, SUM(avail_balance)
FROM accounts
GROUP BY type_id
HAVING SUM(avail_balance) > 10000;
