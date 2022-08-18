/* Assignment3.sql 
   BRANDON CUNNANE
   CS 31A, Summer 2022
*/

/* Set Database. Remove tables if already existing */
USE bank;
DROP TABLE IF EXISTS global_locations;
DROP TABLE IF EXISTS global_locations_backup;
DROP TABLE IF EXISTS employee_pay;


/* Question 1: create global_locations table */
CREATE TABLE global_locations (
	id INT(4),
    loc_name VARCHAR(20),
    address VARCHAR(20),
    city VARCHAR(20),
    zip_postal_code VARCHAR(20),
    phone VARCHAR(15),
    email VARCHAR(15),
    manager_id INT(4),
    emergency_contact VARCHAR(20),
    PRIMARY KEY (id),
    UNIQUE (email)
);
DESCRIBE global_locations;

/* Question 2: Alter the GLOBAL_LOCATIONS table to add a 
column that stores the date of open location.*/
ALTER TABLE global_locations
ADD date_opened DATE;

/* Question 3: Display column names and data types 
for the GLOBAL_LOCATIONS table.*/
DESCRIBE global_locations;

/* Question 4: Delete the date_opened column from the 
GLOBAL_LOCATIONS table.*/
ALTER TABLE global_locations
DROP COLUMN date_opened;

/* Question 5: Rename the GLOBAL_LOCATIONS table as 
GLOBAL_LOCATIONS_BACKUP.*/
ALTER TABLE global_locations
RENAME TO GLOBAL_LOCATIONS_BACKUP;

/* Question 6: Using the column information for the EMPLOYEE_PAY
table below, create the EMPLOYEE_PAY table. Write the syntax you 
will use to create the table. */
CREATE TABLE employee_pay (
	employee_id INT,
    ssn VARCHAR(11),
    salary INT NOT NULL,
    hire_date DATE NOT NULL,
    PRIMARY KEY (employee_id),
    UNIQUE (ssn)
);

/* Question 7: Enter one row into the table. Execute a SELECT * 
statement to verify your input. Refer to the graphic below for input.*/
INSERT INTO employee_pay
VALUES (184167702, '744-04-9444', 5500, '2011-03-15');
SELECT *
FROM employee_pay;

/* Question 8: Display the names of the tables in current database.*/
SHOW tables;

/* Question 9: Add a foreign key constraint named fk_staff_id on 
employee_id column of EMPLOYEE_PAY table referencing to the 
primary key emp_id of EMPLOYEE table.*/
ALTER TABLE  employee_pay
ADD CONSTRAINT fk_staff_id FOREIGN KEY (employee_id) 
REFERENCES employee (emp_id);

/* Question 10: Remove the GLOBAL_LOCATIONS_BACKUP table from the
database. Display the names of the tables in your current database.*/
DROP TABLE IF EXISTS global_locations_backup;
SHOW tables;

/* Question 11: Enter one row into the CATEGORY table. Execute a 
SELECT * statement to verify your input.*/
INSERT INTO category
VALUES ('MMA', 'Money Mark Account');
SELECT *
FROM category;

/* Question 12: Update the misspelled name to “Money Market Account”.*/
UPDATE category
SET category_name = 'Money Market Account'
WHERE category_id = 'MMA';

/* Question 13: Modify the ACCOUNTS table so that clients may not have
more than one account for each account type.
Note: writing as a comment so that it doesn't execute, per discussion board.*/
/*ALTER TABLE accounts
ADD CONSTRAINT one_act_type UNIQUE (type_id, client_id);*/