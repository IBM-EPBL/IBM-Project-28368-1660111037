create database user_details
use user_details
create table details
(
userID int primary key,
username varchar(50),
password varchar(50),
email varchar(50),
rollno int
)
insert into details values (1,'Praveen','praveen@123','praveen@gmail.com',727719EUIT118);
insert into details values (2,'muhil','muhil@123','muhil@gmail.com',727719EUIT099);
insert into details values (3,'naveen','naveen@123','naveen@gmail.com',727719EUIt101);
insert into details values (4,'Sahad','sahad@123','sahad@gmail.com',727719EUIT096);
select * from details
