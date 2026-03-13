create database se;
use se;

create table Student (
	Rollno int primary key,
    Name varchar(50),
    Branch varchar(50)
);

create table Exam (
	Rollno int,
    S_code varchar(10),
    Marks int,
    P_code varchar(10),
    foreign key (Rollno) references Student(Rollno)
);

create table Person (
	First_Name varchar(50),
    Last_Name varchar(50),
    Address varchar(100),
    City varchar(50),
    Age int
);

insert into Person values
('Mickey','Mouse','123 Fantasy Way','Anaheim',73),
('Bat','Man','321 Cavern Ave','Gotham',54),
('Wonder','Woman','987 Truth Way','Paradise',39),
('Donald','Duck','555 Quack Street','Mallard',65),
('Bugs','Bunny','567 Carrot Street','Rascal',58),
('Wiley','Coyote','999 Acme Way','Canyon',61),
('Cat','Woman','234 Purrfect Street','Hairball',32),
('Tweety','Bird','543','Itotitaw',28);

create table Employee (
	Employee_id int primary key,
    First_name varchar(50),
    Last_name varchar(50),
    Salary int,
    Joining_date datetime,
    Department varchar(50)
);

insert into Employee values
(1,'Tisha','Patel',1000000,'2013-01-01 12:00:00','Banking'),
(2,'Devanshi','Lad',800000,'2013-01-01 12:00:00','Insurance'),
(3,'Ekta','Patel',700000,'2013-02-01 12:00:00','Banking'),
(4,'Shriya','Ahir',600000,'2013-02-01 12:00:00','Insurance'),
(5,'Pratham','Bhosle',650000,'2013-02-01 12:00:00','Insurance'),
(6,'Sanket','Ahir',750000,'2013-01-01 12:00:00','Services'),
(7,'Vansh','Patel',650000,'2013-01-01 12:00:00','Services'),
(8,'raj','Patel',600000,'2013-02-01 12:00:00','Insurance'),
(9,'Nishi','Patel',200000,'2013-04-01 12:00:00','Banking'),
(10,'Abhi','Patel',300000,'2013-06-01 12:00:00','Services');

create table Incentive (
    Employee_ref_id int,
    Incentive_date date,
    Incentive_amount int,
    foreign key (Employee_ref_id) references Employee(Employee_id)
);

insert into Incentive values
(1,'2013-02-01',5000),
(2,'2013-02-01',3000),
(3,'2013-02-01',4000),
(1,'2013-01-01',4500),
(2,'2013-01-01',3500);

select First_name as "employee name" from Employee where first_name = 'Tisha';

select First_name, Joining_date, Salary from Employee;

select * from Employee order by First_name asc, Salary desc;

select * from Employee where First_name like '%S%';

select Department, max(Salary) from Employee group by Department order by max(Salary) asc;

select First_name, Incentive_amount from Employee join Incentive on Employee.Employee_id = Incentive.Employee_ref_id where Incentive_amount > 3000;

create table Employee_View (
    Employee_id int,
    First_name varchar(50),
    Last_name varchar(50),
    Salary int
);

create trigger emp_after_insert
after insert
on Employee
for each row
insert into Employee_View
values (new.Employee_id, new.First_name, new.Last_name, new.Salary);

insert into Employee 
values (11,'Dhruv','Patel',500000,'2013-03-01 12:00:00','Banking');

select * from Employee_View;

create table Salesperson (
    SNo int primary key,
    SName varchar(50),
    City varchar(50),
    Comm decimal(4,2)
);

insert into Salesperson values
(1001,'Peel','London',0.12),
(1002,'Serres','San Jose',0.13),
(1004,'Motika','London',0.11),
(1007,'Rafkin','Barcelona',0.15),
(1003,'Axelrod','New York',0.10);

create table Customer (
    CNM int primary key,
    CName varchar(50),
    City varchar(50),
    Rating int,
    SNo int,
    foreign key (SNo) references Salesperson(SNo)
);

INSERT INTO Customer VALUES
(201,'Hoffman','London',100,1001),
(202,'Giovanne','Roe',200,1003),
(203,'Liu','San Jose',300,1002),
(204,'Grass','Barcelona',100,1002),
(206,'Clemens','London',300,1007),
(207,'Pereira','Roe',100,1004);

select * from Orders where Amount > 1000;

select SName, City from Salesperson where City = 'London' and Comm > 0.12;

select * from Salesperson where City = 'Barcelona' or City = 'London';

select * from Salesperson where Comm > 0.10 and Comm < 0.12;

select * from Customer where Rating > 100 or City = 'Rome';