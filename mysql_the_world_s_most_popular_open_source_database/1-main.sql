-- Number of seasons by tvshow_id?
\! echo "\nNumber of seasons by tvshow_id?"
SELECT tvshow_id, count(id) FROM Season GROUP BY tvshow_id;

-- Number of occurrences of the same episode number ordered by episode number?
\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
SELECT DISTINCT number, count(id) FROM Episode GROUP BY number;

-- Top 3 of the Genre's occurrences in all TVShows ordered by this number?
\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
SELECT genre_id, count(genre_id) AS occurrences_genre FROM TVShowGenre GROUP BY genre_id ORDER BY count(genre_id) DESC LIMIT 3;

-- Search all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?
\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
SELECT LOWER(name) AS name FROM TVShow WHERE name LIKE "%th%";
