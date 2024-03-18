			{ "text" : '<!-- Begin MyConnection Server applet -->' }
			{ "regexp" : "/^Visualware MyConnection Server/", "search" : "headers[server]" }
			{ "version" : "/^Visualware MyConnection Server [^\d]+ (\d\.[^\s]+)$/", "search" : "headers[server]" }
			{ "string" : /^Visualware MyConnection Server ([^\d]+) \d\.[^\s]+$/", "search" : "headers[server]" }
