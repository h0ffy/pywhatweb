			{ "search" : "headers[server]", "regexp" : "/^SNARE\/([\d\.]+)$/ }
			{ "search" : "headers[www-authenticate]", "regexp" : "/Digest realm="SNARE"/ }
			{ "version" : "/<H2><CENTER>SNARE Version ([\d\.]+) Status Page<\/H2><\/CENTER>/ }
			{ "certainty" : "75", "text" : '<ADDRESS>Snare Server Remote Control facility</ADDRESS>' }
