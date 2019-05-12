# CEBD1250_repo
Repository for CEBD1250 course

| Name | Date |
|:-------|:---------------|
|Ricardo Rocha|May 05, 2019|

-----

### Resources

My repository includes the following:

- Python scripts for practices 1 and 2 of Class 1: `Practice_1.py` and `Practice_2.py`
- File with answers and SQL commands for questions of Class 2: `CEBD1250_Class_2_Ricardo_Rocha.txt` and `3NF_Exercise_Ricardo_Rocha.xslx`
- File with answers and SQL commands for questions of Class 3: `CEBD1250_Class_3_Ricardo_Rocha.txt` 
- File with answers for questions of Class 4: `CEBD1250_Class_4_Ricardo_Rocha.txt` 

### Class 1 Coding Challenges for Practices 1 and 2

Practice 1
Coding challenges:
 Define a method that ask the user for a number.
  Depending on whether the number is even or odd, print out an appropriate message
 Write a method that takes a number and print its square
 Write a method to convert degrees of Fahrenheit to Celsius

Pactice 2
Coding challenges:
 Create a method that takes a list of numbers. Return the largest number in the list
 Define a method that ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
 Create a method that returns the number of vowels per string.

### Class 2 Questions about the content of the class 

Slide 16
List the entities of our database, can you tell the datatypes that we will be using? Also, could you tell which are the primary and foreign keys

Slide 23
Apply the 3 rd normal form on the following dataset.

Slide 29
In pairs, list the SQL subtypes, defining their purpose
Create the tables course, with fields:
    course_id of type integer,
    course_name of type varchar2 having the size of 50
    course_description of type varchar2 having the size of 100.
Add the field, course_day of type varchar2 of 50.

Slide 34
Return all salaries that are between 40000 and 60000
Get all employees hired after 01-01-1995
Get all salaries from 60000 to 90000
Get all titles where title is equal to engineer

### Class 3 Questions about the content of the class 

Slide 16
Return all salaries that are between 40000 and 60000
Select all employees hired after 01-01-1995
Select all the valid titles names (with to_date = 01-01-9999). Add an extra column written “valid” for the ones with to_date = 01-01-9999, and “not valid” for the ones with
different to_date values
Select all titles where title is equal to engineer

Slide 22
Return the minimum salary of the salary table
What is the difference between “Having” and “Where” clauses?
Return the maximum value for date of birth on the employee table
What is wrong with the following query, re-write it making the needed corrections.
    SELECT employee.emp_no, AVG(salaries.salary)
    FROM employee INNER JOIN salaries AT employee.emp_no = salaries.emp_no
    HAVING AVG(salaries.salary) > 10000
    GROUP BY employee.emp_no

Slide 27
What is the difference between a relational data model and a data warehouse?
Can you tell when to use a data warehouse rather than a normalized database?
Which are the data warehouse phases?
Can you list the importance of the staging phase?

Slide 39
Based on the model below, please define a Multidimensional OLAP model with at least one fact and 4 dimensions

### Class 4 Questions about the content of the class 

Slide 17
Which file structure will be more close to a relational database?
Is AVRO the same thing as JSON, what is the difference?
What is the difference between PARQUET and a delimited file type?
Which kind of compression algorithm allows to consume data using parallel processing?

Slide 21

Define a scenario where ACID properties are needed, enlist 3 reasons why.
Define a scenario where BASE properties are needed, enlist 3 reasons why.

Slide 28
Your client wants to find potential clients based on their locations or interests, what would you suggest?
You need to store the logs from your billing system in a way that they will become easy to access.
You want to analyze the most accessed site of your e-commerce platform over the time. Where would you store the data?
You want to store the inventory of your website contents per endpoints. The page contents will be labelled with the page endpoint accessed, for quick access. Which database solution you would choose?
You have to store financial information about your clients, such as balance account and personal information. Which one you will use?
