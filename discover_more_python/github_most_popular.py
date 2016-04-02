import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token fffa38b10948aa7eff293682308672bc95672ae3'
}

#creating a variable with the response of request
r = requests.get(url = url, headers = request_headers)

print r.content
