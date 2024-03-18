			{ "text" : '<html><body><script>var url="https://"+location.hostname+"/www/index/Slogin.html";location.href=url;</script></body></html>' }
			{ "regexp" : "/^TAC\/Xenta/", "search" : "headers[server]" }
			{ "model" : "/^TAC\/Xenta([\d]{3}|[\d]{3}-[A-Z]{3}) [\d\.]{4}/", "search" : "headers[server]" }
			{ "firmware" : "/^TAC\/Xenta[^\ ]+ ([\d\.]{4})/", "search" : "headers[server]" }
