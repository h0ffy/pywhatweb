			{ "search" : "headers[server]", "model" : "/^(VigorAccess) Web Server$/ }
			{ "search" : "headers[www-authenticate]", "model" : "/^Basic realm="(Login to )?Vigor ([\d]+)"$/", "offset" : "1 }
