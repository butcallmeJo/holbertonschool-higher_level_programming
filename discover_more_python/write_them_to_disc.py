import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token fffa38b10948aa7eff293682308672bc95672ae3'
}

r = requests.get(url, headers = request_headers)

#opening file/deleting old content and writing new content
file_to_disc = open("/tmp/66", 'w')
file_to_disc.truncate()
file_to_disc.write(r.content)

print "The file was saved!"
