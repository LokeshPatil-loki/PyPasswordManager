create table tbl_passwords(
    id int unique auto_increment,
    userid int,
    acc_name varchar(50),
    username varchar(50),
    password varchar(50),
    foreign key (userid) references User(userid),
    primary key (userid,acc_name)
);
