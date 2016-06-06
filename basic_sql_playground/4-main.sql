insert into EyesColor (person_id, color) values (
	(select id from Person where first_name="Jon" and last_name="Snow"),
	"Brown"
);
insert into EyesColor (person_id, color) values (
	(select id from Person where first_name="Arya" and last_name="Stark"),
	"Green"
);

create table "TVShow" (
	id INTEGER PRIMARY KEY NOT NULL,
	name char(128) NOT NULL
);

create table "TVShowPerson" (
	tvshow_id INT NOT NULL,
	person_id INT NOT NULL,
	FOREIGN KEY (tvshow_id) REFERENCES TVShow(id),
	FOREIGN KEY (person_id) REFERENCES Person(id)
);

insert into TVShow (name) values ("Homeland");
insert into TVShow (name) values ("The big bang theory");
insert into TVShow (name) values ("Game of Thrones");
insert into TVShow (name) values ("Breaking bad");

insert into TVShowPerson (tvshow_id, person_id) values (
	(select id from TVShow where name="Breaking bad"),
	(select id from Person where first_name="Walter Junior" and last_name="White")
);
insert into TVShowPerson (tvshow_id, person_id) values (
	(select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Jaime" and last_name="Lannister")
);
insert into TVShowPerson (tvshow_id, person_id) values (
	(select id from TVShow where name="The big bang theory"),
	(select id from Person where first_name="Sheldon" and last_name="Cooper")
);
insert into TVShowPerson (tvshow_id, person_id) values (
	(select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Tyrion" and last_name="Lannister")
);
insert into TVShowPerson (tvshow_id, person_id) values (
	(select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Jon" and last_name="Snow")
);
insert into TVShowPerson (tvshow_id, person_id) values (
	(select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Arya" and last_name="Stark")
);

select * from Person;
select * from EyesColor;
select * from TVShow;
select * from TVShowPerson;
