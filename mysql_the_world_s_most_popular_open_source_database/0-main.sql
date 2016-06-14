-- list all tables:
\! echo "\nList of all tables?"
show tables;

-- displays table structure
\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
show create table TVShow;
show create table Genre;
show create table TVShowGenre;

-- List of TVShows, only id and name ordered by name (A-Z)?
\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
select id, name from TVShow order by name;

-- List of Genres, only id and name ordered by name (Z-A)?
\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
select id, name from Genre order by name desc;

-- List of Network, only id and name?
\! echo "\nList of Network, only id and name?"
select id, name from Network;

-- Number of episodes in the database?
\! echo "\nNumber of episodes in the database?"
select count(id) from Episode;
