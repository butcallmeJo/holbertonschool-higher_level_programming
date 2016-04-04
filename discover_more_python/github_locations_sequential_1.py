import requests, json

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token fffa38b10948aa7eff293682308672bc95672ae3'
}

#creating a variable with the response of request
r = requests.get(url = url, headers = request_headers)
data = json.loads(r.text)
answer = []

users = [{
    'user': i['owner']['login'],
    'full_name': i['full_name']
} for i in data['items']]

for u in users:
    loc_url = "https://api.github.com/users/" + u['user']
    location_r = requests.get(url = loc_url, headers = request_headers)
    u['location'] = location_r.json()['location']
    answer.append({
        'full_name': u['full_name'],
        'location': u['location']
        })

print json.dumps(answer)

# print json.dumps({
#     'location': loc['location'],
#     'full_name': loc['full_name']
#     } for loc in users)

# data = [{
#     'user': u['owner']['login'],
#     'name': u['full_name']
# } for u in r.json()['items']]

# for d in data:
#     loc_url = "https://api.github.com/users/" + d['user']
#     location_r = requests.get(url = loc_url, headers = request_headers)
#     d['location'] = location_r.json()['location']
#     print json.dumps(d['location']) #not working exactly
