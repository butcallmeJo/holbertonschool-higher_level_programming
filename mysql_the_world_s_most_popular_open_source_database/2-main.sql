-- Number of season by TVShow ordered by name (A-Z)?
\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVShow.name, count(Season.tvshow_id) AS nb_seasons FROM TVShow JOIN Season ON (TVShow.id = Season.tvshow_id) GROUP BY Season.tvshow_id ORDER BY name;

-- List of Network by TVShow ordered by name (A-Z)?
\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS "TVShow name", Network.name AS "Network name" FROM TVShow JOIN Network ON (TVShow.network_id = Network.id) ORDER BY TVShow.name;

-- List of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?
\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT name FROM TVShow WHERE network_id = (SELECT id FROM Network WHERE name='Fox (US)') ORDER BY name;

-- Number of episodes by TVShows ordered by name (A-Z)?
\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name AS name, count(Episode.id) AS nb_episodes FROM TVShow JOIN Season ON (TVShow.id = Season.tvshow_id) JOIN Episode ON (Season.id = Episode.season_id) GROUP BY TVShow.id ORDER BY TVShow.name;
