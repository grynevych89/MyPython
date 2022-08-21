-- 1. select-запросы (Запросы на выборку данных)
--==============================================
-- 1.1. Выбрать название всех предметов
select 
    name, id
from 
    Subjects
where 
    id > 1 and id < 6
order by 
    name;
--
-- 2. insert-запросы(запросы на вставку данныъ в таблицу)
--=======================================================
insert into Subjects
    (name)
values
    ('География'),
    ('История'),
    ('Зарубежная литература');
-- 
select * from Subjects;
--
-- 3. delete-запросы (запросы на удаление данных)
--====================
delete 
    from Subjects
where
    id = 18 or id = 15;
--
select * from Subjects;
--
-- 4. update-запросы (запросы на изменение данных)
--==================================================
update Subjects
    set name = 'История Украины'
where
    name = 'История';

--
select * from Subjects;
--