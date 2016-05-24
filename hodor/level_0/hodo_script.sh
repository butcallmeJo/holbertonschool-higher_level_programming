#!/bin/bash
for (( i = 0; i < 1024; i++ )); do
  curl 'http://173.246.108.142/level0.php' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/50.0.2661.102 Chrome/50.0.2661.102 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level0.php' -H 'Connection: keep-alive' --data 'id=1337&holdthedoor=Submit' --compressed
done
