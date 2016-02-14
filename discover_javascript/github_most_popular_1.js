var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token fffa38b10948aa7eff293682308672bc95672ae3'
    }
}

var req = https.request(options, function(res) {
    console.log(res.statusCode);
    res.on('data', function(d) {
	process.stdout.write(d);
    });
});
req.end();
