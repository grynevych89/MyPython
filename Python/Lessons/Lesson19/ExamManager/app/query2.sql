-- ===============================================================
-- DML (Data Manipulation Language) - язык манипулирования данными
-- ===============================================================
-- insert, update, delete

-- ===============================================================
-- DDL (Data Definition Language) - язык определения данных
-- ===============================================================
-- create, alter, drop

-- 1. Создадим таблицу Преподы
-- ---------------------------
create table Teachers (
    id integer primary key autoincrement,
    name text unique,
    birth date  
);
--
insert into Teachers (name, birth) values ('Петя Зубкин', '10.12.2001 14:05:07');
select * from Teachers;
-- 