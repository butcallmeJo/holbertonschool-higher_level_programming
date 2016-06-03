update Person set age=27 where first_name="Jon" AND last_name="Snow";
update Person set age=18 where first_name="Walter Junior" AND last_name="White";
delete from EyesColor where person_id=(select id from Person where first_name="Walter" and last_name="White");
delete from Person where first_name="Walter" AND last_name="White";
select * from Person order by first_name;
