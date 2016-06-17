import MySQLdb

db = MySQLdb.connect(
	"173.246.108.142",
	"student",
	"aLQQLXGQp2rJ4Wy5",
	"Project_169"
)

cursor = db.cursor()
shows = "SELECT TVShow.name, TVShow.id FROM TVShow ORDER BY TVShow.name"
season = "SELECT Season.id, Season.number FROM Season WHERE Season.tvshow_id = "

cursor.execute(shows)
data = cursor.fetchall()

for d in data:
	print d[0] + ":"
	cursor.execute(season + str(d[1]))
	season_data = cursor.fetchall()
	for sd in season_data:
		print "\tSeason " + str(sd[1]) + ":"
		episode = "SELECT Episode.name, Episode.number FROM Episode WHERE Episode.season_id = " + str(sd[0]) + " ORDER BY Episode.number"
		cursor.execute(episode)
		episode_data = cursor.fetchall()
		for ed in episode_data:
			print "\t\t" + str(ed[1]) + ": " + str(ed[0])
