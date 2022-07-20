CREATE TABLE doctors (
id integer PRIMARY KEY,
name varchar(50)
);

--GRANT SELECT ON doctors TO sql_user;

CREATE TABLE work_shifts (
id integer PRIMARY KEY,
name varchar(50),
bonus numeric
);

--GRANT SELECT ON work_shifts TO sql_user;

CREATE TABLE attendances (
id integer PRIMARY KEY,
id_doctor integer,
hours integer,
id_work_shift integer,
FOREIGN KEY (id_doctor) REFERENCES  doctors(id),
FOREIGN KEY (id_work_shift) REFERENCES  work_shifts(id)
);

--GRANT SELECT ON attendances TO sql_user;

insert into doctors (id,name) values
(1,'Arlino'),
(2,'Tiago'),
(3,'Amanda'),
(4,'Wellington');

insert into work_shifts (id,name,bonus) values
(1,'nocturnal',15),
(2,'afternoon',2),
(3,'day',1);

insert into  attendances (id, id_doctor, hours, id_work_shift) values
(1,1,5,1),
(2,3,2,1),
(3,3,3,2),
(4,2,2,3),
(5,1,5,3),
(6,4,1,3),
(7,4,2,1),
(8,3,2,2),
(9,2,4,2);

SELECT doctors.name, round(SUM((attendances.hours * 150.0) + (((attendances.hours * 150.0) * work_shifts.bonus) / 100.0)), 1)
AS salary
FROM doctors
INNER JOIN attendances
ON doctors.id = attendances.id_doctor
INNER JOIN work_shifts
ON work_shifts.id = attendances.id_work_shift 
GROUP BY doctors.id
ORDER BY salary DESC