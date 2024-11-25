CREATE DATABASE university_management_system;
USE university_management_system;

create table pincodes(
	pincode varchar(6) primary key,
    state varchar(255) not null,
    city varchar(255) not null
);



CREATE TABLE departments(
	Dcode INT PRIMARY KEY,
    Dname VARCHAR(100) NOT NULL,
	landmark varchar(255) not null,
    pincode varchar(6),
	Dadd varchar(255) not null,
    foreign key (pincode) references pincodes(pincode)
);

CREATE TABLE Dphones(
	Dcode INT,
    phone VARCHAR(15),
    PRIMARY KEY (Dcode,phone),
    foreign key (Dcode) references departemts(Dcode)
);


create table colleges(
	Cid int primary key,
    Cname varchar(255) not null,
    landmark varchar(255) not null,
    pincode varchar(6),
    Dcode int,
    foreign key (Dcode) references departments(Dcode),
    foreign key (pincode) references pincodes(pincode)
);


CREATE TABLE Cphones(
	Cid INT,
    phone VARCHAR(15),
    PRIMARY KEY (Cid,phone),
    foreign key (Cid) references colleges(Cid)
);


create table instructors(
	Iid int primary key,
    Irank varchar(100) not null,
    fname varchar(100) not null,
    mname varchar(100),
    lname varchar(100),
    age int not null,
    Ioffice varchar(20) not null,
    landmark varchar(255) not null,
    pincode varchar(6),
    Cid int,
    Dcode int,
    foreign key (Dcode) references departments(Dcode),
    foreign key (pincode) references pincodes(pincode),
	foreign key (Cid) references colleges(Cid)
);

CREATE TABLE Iphones(
	Iid INT,
    phone VARCHAR(15),
    PRIMARY KEY (Iid,phone),
    foreign key (Iid) references isntructors(Iid)
);

create table chairMans(
	Dcode int,
    Iid int,
    CstartDate date,
    foreign key (Iid) references isntructors(Iid),
    foreign key (Dcode) references departments(Dcode)
);

create table deans(
	Cid int,
    Iid int,
    foreign key (Cid) references colleges(Cid),
    foreign key (Iid) references isntructors(Iid)
);

create table courses(
	Coid int primary key,
    credits int not null,
    Coname varchar(255) not null,
    Dcode int,
    foreign key (Dcode) references departments(Dcode)
);

create table classRooms(
	C_id int primary key,
    capacity int not null,
	room_no int not null
);


create table sections(
	secid int primary key,
    sem varchar(20),
    year varchar(20),
    ClassRoom_id varchar(50),
    Course_id int,
    Iid int,
    foreign key (ClassRoom_id) references classRooms(C_id),
    foreign key (Course_id) references courses(Coid),
    foreign key (Iid) references isntructors(Iid)
);

create table students(
	Sid int primary key,
    DOB date not null,
    fname varchar(50) not null,
    Mname varchar(50),
    lname varchar (50),
    landmark varchar(100),
    pincode int,
    major varchar(50) not null,
	sec_id int,
    Dcode int,
    foreign key (pincode) references pincodes(pincode),
    foreign key (sec_id) references sections(secid),
    foreign key (Dcode) references departments(Dcode)
);

create table Sphones(
	Sid INT,
    phone VARCHAR(15),
    PRIMARY KEY (Sid,phone),
    foreign key (Sid) references students(Sid)
);


create table results(
	Sid int,
    Coid int,
	grade varchar(5),
    foreign key (Sid) references students(Sid),
    foreign key (Coid) references courses(Coid)
);
