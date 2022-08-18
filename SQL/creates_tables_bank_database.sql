
DROP DATABASE IF EXISTS bank;
CREATE DATABASE bank;
USE bank;

DROP TABLE IF EXISTS account_trans;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS agent;
DROP TABLE IF EXISTS business_client;
DROP TABLE IF EXISTS individual_client;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS account_type;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS branch;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS department;

--
-- The department table
--

CREATE TABLE department (
    dept_id INT NOT NULL,
    dept_name VARCHAR(30) NOT NULL,
    CONSTRAINT dept_id_pk PRIMARY KEY (dept_id)
)  ENGINE=INNODB;

--
-- The jobs table
--
 
CREATE TABLE jobs (
    job_id VARCHAR(10),
    job_title VARCHAR(35) NOT NULL,
    min_salary DECIMAL(6 , 0 ),
    max_salary DECIMAL(6 , 0 ),
    CONSTRAINT job_id_pk PRIMARY KEY (job_id)
)  ENGINE=INNODB;

--
-- The location table
--

CREATE TABLE location (
    location_id INT(11) NOT NULL,
    city VARCHAR(45) DEFAULT NULL,
    state CHAR(2) DEFAULT NULL,
    zip_code INT(11) DEFAULT NULL,
    country_name VARCHAR(10) DEFAULT NULL,
    PRIMARY KEY (location_id)
)  ENGINE=INNODB;

--
-- The branch table
--

CREATE TABLE branch (
    branch_id INT NOT NULL,
    branch_name VARCHAR(20) NOT NULL,
    address VARCHAR(50),
    loc_id INT(11),
    CONSTRAINT branch_id_pk PRIMARY KEY (branch_id),
    CONSTRAINT bran_loc_fk FOREIGN KEY (loc_id)
        REFERENCES location (location_id)
)  ENGINE=INNODB;

--
-- The employee table
--

CREATE TABLE employee (
    emp_id INT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    manager_id INT,
    dept_id INT,
    job_id VARCHAR(10),
    branch_id INT,
    CONSTRAINT fk_emp_id FOREIGN KEY (manager_id)
        REFERENCES employee (emp_id),
    CONSTRAINT fk_dept_id FOREIGN KEY (dept_id)
        REFERENCES department (dept_id),
    CONSTRAINT fk_branch_id FOREIGN KEY (branch_id)
        REFERENCES branch (branch_id),
    CONSTRAINT pk_employee PRIMARY KEY (emp_id),
    CONSTRAINT job_emp_fk FOREIGN KEY (job_id)
        REFERENCES jobs (job_id)
)  ENGINE=INNODB;

--
-- The category table
--
CREATE TABLE category (
    category_id VARCHAR(10) NOT NULL,
    category_name VARCHAR(45) DEFAULT NULL,
    PRIMARY KEY (category_id)
)  ENGINE=INNODB;

--
-- The account_type table
--

CREATE TABLE account_type (
    type_id VARCHAR(10) NOT NULL,
    account_name VARCHAR(50) NOT NULL,
    category_id VARCHAR(10) NOT NULL,
    date_offered DATE,
    date_ended DATE,
    CONSTRAINT fk_type_id FOREIGN KEY (category_id)
        REFERENCES category (category_id),
    CONSTRAINT type_id_pk PRIMARY KEY (type_id)
)  ENGINE=INNODB;

--
-- The clients table
--

CREATE TABLE clients (
    client_id INT,
    fed_id VARCHAR(12) NOT NULL,
    client_type_id VARCHAR(2),
    address VARCHAR(60),
    loc_id INT(11),
    phone_number VARCHAR(15) NOT NULL,
    CONSTRAINT bran_loc_fk1 FOREIGN KEY (loc_id)
        REFERENCES location (location_id),
    CONSTRAINT clients_pk PRIMARY KEY (client_id)
)  ENGINE=INNODB;

--
-- The individual_client table
--

CREATE TABLE individual_client (
    client_id INT NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    birth_date DATE,
    CONSTRAINT fk_i_client_id FOREIGN KEY (client_id)
        REFERENCES clients (client_id),
    CONSTRAINT individual_pk PRIMARY KEY (client_id)
)  ENGINE=INNODB;

--
-- The  business_clien table
--

CREATE TABLE business_client (
    client_id INT NOT NULL,
    bus_name VARCHAR(40) NOT NULL,
    state_id VARCHAR(10) NOT NULL,
    start_date DATE,
    CONSTRAINT fk_b_client_id FOREIGN KEY (client_id)
        REFERENCES clients (client_id),
    CONSTRAINT business_pk PRIMARY KEY (client_id)
)  ENGINE=INNODB;


--
-- The agent table
--
CREATE TABLE agent (
    agent_id INT NOT NULL,
    client_id INT NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    title VARCHAR(20),
    CONSTRAINT fk_agent_id FOREIGN KEY (client_id)
        REFERENCES business_client (client_id),
    CONSTRAINT agent_pk PRIMARY KEY (agent_id)
)  ENGINE=INNODB;


--
-- The accounts table
--
CREATE TABLE accounts (
    account_id INT NOT NULL,
    type_id VARCHAR(10) NOT NULL,
    client_id INT NOT NULL,
    created DATE NOT NULL,
    close_date DATE,
    last_activity_date DATE,
    a_status ENUM('ACTIVE', 'CLOSED', 'CANCELLED'),
    branch_id INT,
    open_emp_id INT,
    avail_balance DECIMAL(10 , 2 ),
    pending_balance DECIMAL(10 , 2 ),
    PRIMARY KEY (account_id),
    CONSTRAINT fk_a_type_id FOREIGN KEY (type_id)
        REFERENCES account_type (type_id),
    CONSTRAINT fk_a_client_id FOREIGN KEY (client_id)
        REFERENCES clients (client_id),
    CONSTRAINT fk_a_branch_id FOREIGN KEY (branch_id)
        REFERENCES branch (branch_id),
    CONSTRAINT fk_a_emp_id FOREIGN KEY (open_emp_id)
        REFERENCES employee (emp_id)
)  ENGINE=INNODB;


--
-- The account_trans table
--
CREATE TABLE account_trans (
    trans_id INT,
    trans_date DATETIME NOT NULL,
    account_id INT NOT NULL,
    trans_type ENUM('DBT', 'CDT'),
    amount DECIMAL(10 , 2 ) NOT NULL,
    teller_id INT,
    branch_id INT,
    avail_date DATETIME,
    CONSTRAINT fk_at_account_id FOREIGN KEY (account_id)
        REFERENCES accounts (account_id),
    CONSTRAINT fk_teller_emp_id FOREIGN KEY (teller_id)
        REFERENCES employee (emp_id),
    CONSTRAINT fk_exec_branch_id FOREIGN KEY (branch_id)
        REFERENCES branch (branch_id),
    CONSTRAINT trans_pk PRIMARY KEY (trans_id)
)  ENGINE=INNODB;