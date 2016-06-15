-- List of TVShows ordered by name (A-Z) with more than or equal 4 seasons?
\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT TVShow.name FROM TVShow JOIN Season ON (TVShow.id = Season.tvshow_id) GROUP BY Season.tvshow_id HAVING COUNT(Season.id) > 3 ORDER BY name;

-- List of TVShows ordered by name (A-Z) with the Genre 'Comedy'?
\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT TVShow.name FROM TVShow JOIN TVShowGenre ON (TVShow.id = TVShowGenre.tvshow_id) JOIN Genre ON (TVShowGenre.genre_id = Genre.id) WHERE Genre.name = 'Comedy' ORDER BY name;

-- List of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?
\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT Actor.name FROM Actor JOIN TVShowActor ON (Actor.id = TVShowActor.actor_id) JOIN TVShow ON (TVShowActor.tvshow_id = TVShow.id) WHERE TVShow.name = 'The Big Bang Theory' ORDER BY name;

-- Top 10 of actors by number of TVShows where they are? (without Actor name order => can be random)
\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT Actor.name, COUNT(TVShow.id) as nb_tvshows FROM TVShow JOIN TVShowActor ON (TVShow.id = TVShowActor.tvshow_id) JOIN Actor ON (TVShowActor.actor_id = Actor.id) GROUP BY Actor.name ORDER BY COUNT(TVShow.id) DESC LIMIT 10;
