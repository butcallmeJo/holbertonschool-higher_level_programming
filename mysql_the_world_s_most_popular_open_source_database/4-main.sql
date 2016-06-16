-- List of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)
\! echo "List of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)"
SELECT Genre.name AS "Genre name", TVShow.name AS "TVShow name" FROM TVShow RIGHT JOIN TVShowGenre ON (TVShow.id = TVShowGenre.tvshow_id) RIGHT JOIN Genre ON (TVShowGenre.genre_id = Genre.id) ORDER BY Genre.name;
