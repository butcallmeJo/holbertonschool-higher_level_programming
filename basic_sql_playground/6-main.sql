select name, sum(age) sum_age from Person P
	inner join TVShowPerson TVSP on P.id=TVSP.person_id
	inner join TVShow TVS on TVS.id=TVSP.tvshow_id
	group by TVS.name order by sum_age
;

select name, first_name, last_name, min(age) from Person P
	inner join TVShowPerson TVSP on P.id=TVSP.person_id
	inner join TVShow TVS on TVS.id=TVSP.tvshow_id
	group by TVS.name order by age
;
