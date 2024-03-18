			{ "search" : "headers[server]", "version" : "/^Alpha Five( Application Server)?\/([\d\.]+ Build\/[\d\-]+)/", "offset" : "1 }
			{ "search" : "headers[set-cookie]", "regexp" : "/A5wSessionId=[a-f\d]{32};/ }
			{ "search" : "headers[set-cookie]", "regexp" : "/A5wBrowserId=[a-f\d]{32};/ }
