require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token fffa38b10948aa7eff293682308672bc95672ae3'
}

http = HTTPClient.new
response = http.get_content("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc", nil, extheaders)

json = JSON.parse(response)

# puts json["items"][0]["full_name"]

json["items"].map {|n| puts n["full_name"] n["location"]}
