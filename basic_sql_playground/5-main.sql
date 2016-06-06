select distinct last_name from Person
	join (select tvshow_id, person_id as id from TVShowPerson) using (id)
	where tvshow_id=(select id from TVShow where name="Game of Thrones");

select count(*) from Person where age>30;

select P.id, first_name, last_name, age, color, name from Person P
	inner join EyesColor E on P.id=E.person_id
	inner join TVShowPerson TVSP on P.id=TVSP.person_id
	inner join TVShow TVS on TVS.id=TVSP.tvshow_id
;
select sum(age) from Person;
