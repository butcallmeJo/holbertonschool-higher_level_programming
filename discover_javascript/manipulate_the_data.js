var https = require('https');
var fs = require('fs')

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token fffa38b10948aa7eff293682308672bc95672ae3'
    }
}


function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}


var req = https.request(options, function (res) {
    streamToString(res, (jsonString) => {
	var parsedString = JSON.parse(jsonString);
	var output = parsedString.items.map(function(input) {
	    return input.full_name;
	}).join("\n");
	console.log(output);

	fs.writeFile("/tmp/13", jsonString, (err) => {
	    if(err)
		return console.log(err);
	});
    });

});
req.end();
