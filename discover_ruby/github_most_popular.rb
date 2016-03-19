require 'httpclient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token fffa38b10948aa7eff293682308672bc95672ae3'
}

http = HTTPClient.new
response = http.get_content("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc", nil, extheaders)

puts response
