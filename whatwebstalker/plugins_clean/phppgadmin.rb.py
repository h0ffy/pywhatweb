			{ "name" : "PPA_ID Cookie", "search" : "headers[set-cookie]", "regexp" : "/^PPA_ID=[a-z0-9]+/ }
			{ "text" : '<td><span class="appname">phpPgAdmin</span></td>' }
			{ "version" : "%r{<span class="appname">phpPgAdmin</span> <span class="version">([\d\.]+)</span>} }
