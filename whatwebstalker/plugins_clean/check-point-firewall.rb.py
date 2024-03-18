			{ "search" : "headers[location]", "regexp" : "/\/fwauthredirect[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}id[\d]+$/ }
			{ "status" : "401", "string" : /FW-1 at ([^\s]+): Unauthorized to access the document\./ }
